# Monte Carlo Simulator

## Metadata
Monte Carlo Simulator is a Python package for simulation of random events like die and coins. By Will Tenpas (wet9me).

## Synopsis
### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install montecarlo.

```bash
pip install montecarlo
```

### Using Classes

```python
from montecarlo.montecarlo import *
import montecarlo.montecarlo as mc

# creates a six-sided die with faces from an np.array
die = Die(np.array([1,2,3,4,5,6])

# creates a game out of a list of Die objects
die_list = [die]*5
game = Game(die_list)

# analyzes a given Game that has rolled its Die
game.roll(500)
analysis = Analyzer(game)
```

## API Description
### Die Class
#### Change Weight
```python
die.change_weight(face, new_weight)
'''
ARGS: 
face: takes str or number depending on type of faces.
new_weight: takes number type.
DESCRIPTION: 
Takes the face whose weight you want to be changed and assign its new weight. Reassigns weights for given face values after checking their types.
Weight must be a numeric type.
'''
```
#### Roll Die
```python
die.roll_die(num_rolls=1)
'''ARGS:
num_rolls: defaults to 1, takes integer and rolls the die that many times.
DESCRIPTION:
Rolls the dice a specified amount of times and returns an unstored list of results.'''
```
#### Die State
```python
die.die_state()
'''ARGS:
none
DESCRIPTION:
Returns a deep copy of the die_info data frame.'''
```

### Game Class
#### Play
```python
game.play(num_rolls)
'''ARGS:
num_rolls: takes integer to determine how many rolls are to be conducted.
DESCRIPTION:
Creates a dataframe of roll results with the roll number in the index and each column representing a die object. The cell values then have the face rolled from each die on that roll.'''
```
#### Return Play
```python
game.return_play(format='wide')

'''ARGS:
format: takes string either 'wide' or 'narrow', defaults to wide.
DESCRIPTION:
Returns a wide or narrow data frame with the results from the rolls. If narrow, the index is a multi index
composed of the roll and die number.'''
```

### Analyzer Class
#### Jackpot
```python
analyzer.jackpot()
'''ARGS:
none
DESCRIPTION:
Returns an integer of the instances where every die rolled hits the same face.'''

#### Face Counts
```python
analyzer.facecounts
'''ARGS:
none
DESCRIPTION:
Returns a data frame of results for each face. Each row represents a roll
and each column represents a face. The individual cell values represent the
number of dies that landed on that face had in that particular roll.'''
```
#### Combonation Counts
```python
analyzer.combocount()
'''ARGS:
none
DESCRIPTION:
Returns a data frame of unique combinations from the results data frame. The index is the combination and the first column is the count that that combination was rolled.'''

#### Permutation Counts
```python
analyzer.permcount()
'''ARGS:
none
DESCRIPTION:
Returns a data frame of unique permutations from the results data frame.
The index is the permutation and the first column is the count that that
permutation was rolled.'''
```

## Full Doc Strings
    class Analyzer(builtins.object)
     |  Analyzer(game)
     |  
     |  The class is used to analyze played games for overall results as well as special cases
     |  
     |  Methods defined here:
     |  
     |  __init__(self, game)
     |      ARGS:
     |      game: a single game object.
     |      DESCRIPTION:
     |      Initializes analyzer and verifies game object type.
     |  
     |  combocount(self)
     |      ARGS:
     |      none
     |      DESCRIPTION:
     |      Returns a data frame of unique combinations from the results data frame.
     |      The index is the combination and the first column is the count that that
     |      combination was rolled.
     |  
     |  facecounts(self)
     |      ARGS:
     |      none
     |      DESCRIPTION:
     |      Returns a data frame of results for each face. Each row represents a roll
     |      and each column represents a face. The individual cell values represent the
     |      number of dies that landed on that face had in that particular roll.
     |  
     |  jackpot(self)
     |      ARGS:
     |      none
     |      DESCRIPTION:
     |      Returns an integer of the instances where every die rolled hits the same face.
     |  
     |  permcount(self)
     |      ARGS:
     |      none
     |      DESCRIPTION:
     |      Returns a data frame of unique permutations from the results data frame.
     |      The index is the permutation and the first column is the count that that
     |      permutation was rolled.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Die(builtins.object)
     |  Die(faces)
     |  
     |  This class is used to create, modify, and roll die.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, faces)
     |      ARGS: faces, takes an np.array.
     |      DESCRIPTION: 
     |      Initializes the faces and assigns initial weights as while as checking for data types. Turns the array
     |      into a dataframe with faces for index and weight values, initially set to 1, in a column. Supplied array must have distinct values in string or 
     |      number format.
     |  
     |  change_weight(self, face, new_weight)
     |      ARGS: 
     |      face: takes str or number depending on type of faces.
     |      new_weight: takes number type.
     |      DESCRIPTION: 
     |      Takes the face you want to be changed and its new weight. Reassigns weights for given face values after checking their types.
     |      Weight must be a numeric type.
     |  
     |  die_state(self)
     |      ARGS:
     |      none
     |      DESCRIPTION:
     |      Returns a deep copy of the die_info data frame.
     |  
     |  roll_die(self, num_rolls=1)
     |      ARGS:
     |      num_rolls: defaults to 1, takes integer.
     |      DESCRIPTION:
     |      Rolls the dice a specified amount of times and returns an unstored list of results.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Game(builtins.object)
     |  Game(die_list)
     |  
     |  This class is used to roll multiple die of the same length at once
     |  
     |  Methods defined here:
     |  
     |  __init__(self, die_list)
     |      ARGS:
     |      die_list: list of die objects, created using Die().
     |      DESCRIPTION:
     |      Initializes game and verifies die list.
     |  
     |  play(self, num_rolls)
     |      ARGS:
     |      num_rolls: takes integer to determine how many rolls are to be conducted.
     |      DESCRIPTION:
     |      Creates a dataframe of roll results with the roll number in the index and each column representing a die object. The
     |      cell values then have the face rolled from each die on that roll.
     |  
     |  return_play(self, format='wide')
     |      ARGS:
     |      format: takes string either 'wide' or 'narrow', defaults to wide.
     |      DESCRIPTION:
     |      Returns a wide or narrow data frame with the results from the rolls. If narrow, the index is a multi index
     |      composed of the roll and die number.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

## License

[MIT](https://choosealicense.com/licenses/mit/)