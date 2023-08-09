import numpy as np
import pandas as pd
import copy

'''Class docstrings should describe the general purpose of the class.

Method docstrings should describe the purpose of the method, any input arguments, any return values if applicable, and any changes to the object’s state that the user should know about.

Input argument descriptions should describe data types and formats as well as any default values.'''

class Die():
    def __init__(self, faces):
        '''Initializes the faces and assigns initial weights as while as checking for data types'''
        # checking that it is a numpy array
        if type(faces) != type(np.array([])):
            raise TypeError("That's not an array!")
        #checking that the type of the array is string or number
        if not np.issubdtype(faces.dtype, np.str_) and not np.issubdtype(faces.dtype, np.number):
            raise TypeError("The array must have strings or numbers!")
        #checking that the array has distinct values by making array a set
        if len(faces)!=len(set(faces)):
            raise ValueError("Array must have distinct values!")
        #initializes weights to be 1 for each face
        weights = [1 for i in faces]
        #creates private DF for weights and faces
        self._die_info = pd.DataFrame({'Weights':weights}, index=faces)
    def change_weight(self, face, new_weight):
        '''Reassigns weights for given face values after checking their types'''
        if face not in self._die_info.index:
            raise IndexError("The given face value is not present in the die.")
        if not np.issubdtype(type(new_weight), np.number):
            raise TypeError("The new weight must be a numeric type.")
        self._die_info.loc[face, 'Weights'] = new_weight
    def roll_die(self, num_rolls=1):
        '''rolls the dice a specified amount of times and returns an unstored list of results'''
        return([np.random.choice(self._die_info.index, size=1, p=self._die_info['Weights'] / self._die_info['Weights'].sum())[0] for i in range(num_rolls)])
    def die_state(self):
        '''returns a shallow copy of the die_info'''
        copy_die_info = copy.deepcopy(self._die_info)
        return(copy_die_info)

class Game():
    def __init__(self, die_list):
        '''initializes game and checks die list'''
        self.die_list = die_list
        if not all(isinstance(die,Die) for die in die_list):
            raise ValueError("Your list doesn't have all die in it!")
        faces = die_list[0].die_state()
        face_values = set(faces.index)
        for i in die_list:
            test_faces_df = i.die_state()
            if set(test_faces_df.index)!=face_values:
                raise ValueError("The faces on your dice are different!")
    def play(self, num_rolls):
        '''creates a set of rolls from the supplied die list'''
        _results_df = pd.DataFrame(index=range(num_rolls))
        for i in range(len(self.die_list)):
            results = self.die_list[i].roll_die(num_rolls)
            _results_df[i] = results
        self._results_df = _results_df.rename_axis("Roll", axis=0)
        return(self._results_df)
    def return_play(self, format='wide'):
        '''returns a wide or narrow data frame with the results from the rolls'''
        if format != 'wide' and format!='narrow':
            raise ValueError("You've supplied an invalid format type!")
        if format=='narrow':
            narrow_df = self._results_df.stack()
            # INVESTIGATE THIS MORE, NEED TO RENAME THE COLUMN IN PLAY TO HAVE A HEADER FOR DIE
            return(narrow_df.index)
        copy_roll_results = copy.deepcopy(self._results_df)

class Analyzer():
    def __init__(self, game):
        '''initializes the analyzer and checks for a game'''
        if not isinstance(game, Game):
            raise ValueError("You have not supplied a game!")
        self.game = game
        self.die_list = self.game.die_list
    def jackpot(self):
        '''counts how many times all the die objects were equal on the same roll'''
        _results_df = self.game._results_df
        jackpot_count = 0
        print(_results_df)
        for row in _results_df.index:
            rolls = _results_df.loc[row]
            jackpot = all(value==rolls.loc[0] == value for value in rolls)
            jackpot_count += jackpot
        return(jackpot_count)
    def facecounts(self):
        '''returns a dataframe with a count for each face and how many times it was rolled in each roll'''
        _results_df = self.game._results_df
        faces = self.die_list[0].die_state().index
        facecounts_df = pd.DataFrame(columns=faces, index = _results_df.index)
        print(faces)
        for index, roll in _results_df.iterrows():
            rolls = pd.Series(roll.values)
            counts = rolls.value_counts().reindex(facecounts_df.columns, fill_value=0)
            facecounts_df.loc[index] = counts
        return(facecounts_df)
    def combocount(self):
        '''returns a dataframe with a multi index of distinct combinations with their number of counts'''
        #combinations don't care about order so H,T is the same as T,H
        _results_df = self.game._results_df
        #sort each combo so that T,H and H,T both become H,T, then make the results a tuple
        comb_list = []
        for row in _results_df.values:
            tuprow = tuple(sorted(row))
            comb_list.append(tuprow)
        #then we create a set of this combo_list so that we only get unique combos
        unique_comb = set(comb_list)
        #now we do a count on the set and make a dictionary with the combo as the key and the count as the value
        comb_counts = {comb: comb_list.count(comb) for comb in unique_comb}
        #then we go thorugh and put this into a dataframe
        comb_df = pd.DataFrame(comb_counts.items(), columns=['Combination', 'Count'])
        return(comb_df)
    def permcount(self):
        '''returns a dataframe with a multi index of distinct permutations with their number of counts'''
        _results_df = self.game._results_df
        #need to conver each row entry into tuples, where the cell entry is an entry in the tuple
        perm_list = list(map(tuple, _results_df.values))
        #then we create a set of this perm_list so that we only get unique permutations
        unique_permutations = set(perm_list)
        #now we do a count on the set and make a dictionary with the permutation as the key and the ocunt as the value
        perm_counts = {perm: perm_list.count(perm) for perm in unique_permutations}
        #then we go thorugh and put this into a dataframe
        perm_df = pd.DataFrame(perm_counts.items(), columns=['Permutation', 'Count'])
        return(perm_df)
