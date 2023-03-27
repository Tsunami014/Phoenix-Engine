import unittest
import side as s

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

        s.run_action("C*S*apple = {3}", ['a', 'b', [0, 1, 2, 3], None])
        self.assertEqual(g.apple, 0)
        
        s.run_action("C*S*apple = int('{3}')", ['a', 'b', [5, 10], 'c'])
        self.assertEqual(g.apple, 5)
        
        self.assertRaises(IndexError, s.run_action, "C*S*apple = '{5}'", ['a', 'b', [0, 1, 2, 3], None])
        
        #self.assertRaises(NameError, s.run_action, "C*S*apple = '{5}'", ['a', 'b', [0, 1, 2, 3], None])

if __name__ == '__main__':
    unittest.main()