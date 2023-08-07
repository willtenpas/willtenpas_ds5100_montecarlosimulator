import numpy as np
import pandas as pd
import copy

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
        '''creates a set of rolls'''
        _results_df = pd.DataFrame(index=range(num_rolls))
        for i in range(len(self.die_list)):
            results = self.die_list[i].roll_die(num_rolls)
            _results_df[i] = results
        self._results_df = _results_df.rename_axis("Roll", axis=0)
        return(self._results_df)
    def return_play(self, format='wide'):
        if format != 'wide' and format!='narrow':
            raise ValueError("You've supplied an invalid format type!")
        if format=='narrow':
            narrow_df = self._results_df.stack()
            return(narrow_df.index)
        copy_roll_results = copy.deepcopy(self._results_df)
    


exampleDie1 = Die(np.array([1,2,3,4,5,6]))
exampleDie2 = Die(np.array([1,2,3,4,5,6]))
dieList = [exampleDie1, exampleDie2]
testgame = Game(dieList)
testgame.play(4)
print(testgame.return_play(format='narrow'))

