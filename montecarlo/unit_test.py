import unittest
from montecarlo import Die,Game,Analyzer
import montecarlo
import numpy as np
import pandas as pd
import pandas._testing as pd_testing

class monte_test_case(unittest.TestCase):
    def setUp(self):
        self.die1 = Die(np.array([1, 2, 3, 4]))
        self.die2 = Die(np.array([1, 2, 3, 4]))
        self.die3 = Die(np.array([1, 2, 3, 4]))
        self.buggy_die = [self.die1, Die(np.array([1,2,3,5]))]
        self.game1 = Game([self.die1, self.die2])
        self.game1.play(100)
        self.anal1 = Analyzer(self.game1)
    def test_1_die_weights(self):
        '''test of die init to check data frame'''
        test_value = isinstance(self.die1._die_info, pd.DataFrame)
        message = 'Die initialization is not creating data frame.'
        self.assertTrue(test_value, message)
    def test_2_change_weight(self):
        '''test of change weight for new weight'''
        self.die1.change_weight(1,2)
        expected = pd.DataFrame({'Weights':[2,1,1,1]},index=[1,2,3,4])
        message = 'Die weights are not being changed.'
        pd_testing.assert_frame_equal(self.die1._die_info, expected, check_dtype=False, check_index_type=False)
    def test_3_roll(self):
        '''test of change weight for new weight'''
        test_value = type([])
        message = 'Die roll is not returning list.'
        self.assertEqual(type(self.die1.roll_die()),test_value, message)
    def test_4_d_state(self):
        '''test of change weight for new weight'''
        test_value = type(pd.DataFrame())
        message = 'Die roll is not returning data frame.'
        self.assertEqual(type(self.die1.die_state()),test_value, message)
    def test_5_g_init(self):
        '''test of game initialization to see if you get correct error'''
        message = 'Game allows you to supply improper die!'
        with self.assertRaises(ValueError) as context:
            Game(self.buggy_die)
        self.assertEqual(str(context.exception), 'The faces on your dice are different!')
    def test_6_play(self):
        '''test of type returned by playing game'''
        test_value = type(pd.DataFrame())
        message = 'Game play is not returning data frame.'
        self.assertEqual(type(self.game1.play(4)),test_value, message)
    def test_7_return_play(self):
        '''test of type returned by game play'''
        test_value = type(pd.DataFrame())
        message = 'Game play is not returning data frame.'
        self.assertEqual(type(self.game1.return_play()),test_value, message)  
    def test_8_anal_init(self):
        '''test of analyzer initialization to see if you can supply non games'''
        message = 'You have not supplied a game!'
        with self.assertRaises(ValueError) as context:
            Analyzer(pd.DataFrame)
        self.assertEqual(str(context.exception), 'You have not supplied a game!')
    def test_9_anal_jack(self):
        '''test of type returned by jackpot analyzer'''
        test_value = type(3)
        message = 'Jackpot analysis is not returning an integer!'
        self.assertEqual(type(self.anal1.jackpot()),test_value, message)
    def test_10_anal_face(self):
        '''test of type returned by game play'''
        test_value = type(pd.DataFrame())
        message = 'Face count analysis is not returning a dataframe!'
        self.assertEqual(type(self.anal1.facecounts()),test_value, message)
    def test_11_anal_comb(self):
        '''test of type returned by comb count'''
        test_value = type(pd.DataFrame())
        message = 'Comb counter analysis is not returning a dataframe!'
        self.assertEqual(type(self.anal1.combocount()),test_value, message)
    def test_12_anal_perm(self):
        '''test of type returned by perm count'''
        test_value = type(pd.DataFrame())
        message = 'Perm counter analysis is not returning a dataframe!'
        self.assertEqual(type(self.anal1.permcount()),test_value, message)
if __name__ =='__main__':
    unittest.main(verbosity=3)