import unittest
import redo_side as s
from json import load, loads

"""
Action code:
    (split by ';', so '00Hello;01Goodbye' are 2 different statements both executed seperately)
    
    First number:
        0 = print
        1 = set variable (if not exists then create variable)
        2 = delete variable
    
    Second number:
        with the set variables:
            0 = global
            1 = class
        with the print:
            what colour
        with the delete variables:
            0 = the object specified
    
    Third string (not for first number=2):
        what variable name/what to print
    
    Delimeter: " ~ "
    
    Fourth number (only for first number=1):
        what value to set it to
            0 = the closest exit to what was said
"""

class NewTest(unittest.TestCase):
    g = s.Game()
    
    def test_closest_num(self):
        self.assertEqual(s.closest_num(list(range(10)), 2), 2) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(s.closest_num(list(range(0, 10, 2)), 6), 6) # [0, 2, 4, 6, 8] 
        self.assertEqual(s.closest_num(list(range(0, 10, 4)), 3), 4) # [0, 4, 8]
        self.assertEqual(s.closest_num(list(range(0, 10, 5)), 1), 0) # [0, 5]
        self.assertEqual(s.closest_num(list(range(0, 10, 5)), 3), None) # [0, 5]
        self.assertEqual(s.closest_num(list(range(0, 10, 5)), 4), 5) # [0, 5]
    
    def test_parsing(self):
        tests = load(open('test cases/parse tests.json'))
        for test in tests.keys():
            self.assertEqual(self.g.parse(tests[test]), loads(test))
    
    def test_action(self):
        #TODO: finish this test
        self.assertEqual(self.g.run({'action': ['throw'], 'subjobj': [('pot', {'det': 'the'})]}, [{'subjobj': 1, 'action': 'abcdefg'}, {'subj': 2, 'action': 12345}]), 'abcdefg')
        self.assertEqual(self.g.run({'action': ['say'], 'subj': [('jeff'), ('joe')]}, [{'subjobj': 1, 'action': 'abcdefg'}, {'subj': 2, 'action': 12345}]), '12345')
        self.assertEqual(self.g.run({'action': ['talk'], 'subj': [('jeff')]}, [{'subjobj': 1, 'action': 'abcdefg'}, {'subj': 2, 'action': 12345}]), None)
        self.assertEqual(self.g.run({'action': ['die'], 'in': [('hole')]}, [{'subjobj': 1, 'action': 'abcdefg'}, {'subj': 2, 'action': 12345}]), None)

class MainGameTest(unittest.TestCase):
    
    def test_closest_num(self):
        self.assertEqual(s.closest_num(list(range(10)), 2), 2) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(s.closest_num(list(range(0, 10, 2)), 6), 6) # [0, 2, 4, 6, 8] 
        self.assertEqual(s.closest_num(list(range(0, 10, 4)), 3), 4) # [0, 4, 8]
        self.assertEqual(s.closest_num(list(range(0, 10, 5)), 1), 0) # [0, 5]
        self.assertEqual(s.closest_num(list(range(0, 10, 5)), 3), None) # [0, 5]
        self.assertEqual(s.closest_num(list(range(0, 10, 5)), 4), 5) # [0, 5]
    
    def test_run_action(self):
        g = s.Game()
        g.run_action("C*S*apple = '{1}'", ['a', 'b', 'c'], set_values_3=False)
        self.assertEqual(g.apple, 'b')

        g.run_action("C*S*apple = {3}", ['a', 'b', [0, 1, 2, 3], None])
        self.assertEqual(g.apple, 0)
        
        g.run_action("C*S*apple = int('{3}')", ['a', 'b', [5, 10], 'c'])
        self.assertEqual(g.apple, 5)
        
        self.assertRaises(IndexError, g.run_action, "C*S*apple = '{5}'", ['a', 'b', [0, 1, 2, 3], None])
        
        #self.assertRaises(NameError, g.run_action, "C*S*apple = '{5}'", ['a', 'b', [0, 1, 2, 3], None])

if __name__ == '__main__':
    unittest.main()