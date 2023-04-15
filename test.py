import unittest
import side as s
from json import loads
import re, ast

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

# print('"'+str([g.to_tree(sent.root) for sent in s.nlp("throw the pot").sents][0]).replace('(', '[').replace(')', ']')+'"'")
# please note that the g.to_tree function uses tuples, so the code above replaces those with lists, so there shouldn't be any difference

class NewTest(unittest.TestCase):
    g = s.Game()
    
    def test_closest_num(self):
        self.assertEqual(s.closest_num(list(range(10)), 2), 2) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(s.closest_num(list(range(0, 10, 2)), 6), 6) # [0, 2, 4, 6, 8] 
        self.assertEqual(s.closest_num(list(range(0, 10, 4)), 3), 4) # [0, 4, 8]
        self.assertEqual(s.closest_num(list(range(0, 10, 5)), 1), 0) # [0, 5]
        self.assertEqual(s.closest_num(list(range(0, 10, 5)), 3), None) # [0, 5]
        self.assertEqual(s.closest_num(list(range(0, 10, 5)), 4), 5) # [0, 5]
        
    #TODO: test self.g.parse_word
    
    def test_parsing(self):
        with open('test cases/parse tests.json') as f:
            tests = loads(f.read())
            f.close()
        for test in tests.keys():
            #trees = [self.g.to_tree(sent.root) for sent in s.nlp("I took my dog for a walk").sents]
            testcase = tests[test].replace("'", '"')
            #just a little reg expression to make the test case work
            for match in re.findall(r"\[[^[]+?](?=:)", testcase):
                testcase = testcase.replace(match, '(%s)' % match[1:-1])
            
            res = self.g.parse(ast.literal_eval(testcase))
            print(self.g.log)
            self.assertEqual(res, loads(test.replace("'", '"')))
    
    def test_action(self):
        #TODO: finish this test
        #please note this is testing material the real inputs/outputs are different
        self.assertEqual(self.g.action({'action': ['throw'], 'subjobj': [('pot', {'det': 'the'})]}, {'subjobj': 1, 'action': 'abcdefg'}), 'abcdefg')
        self.assertEqual(self.g.action({'action': ['say'], 'subj': [('jeff'), ('joe')]}, {'subj': 2, 'action': '12345'}), '12345')
        self.assertEqual(self.g.action({'action': ['talk'], 'subj': [('jeff')]}, {'subjobj': 1, 'action': 'abcdefg'}), None)
        self.assertEqual(self.g.action({'action': ['die'], 'in': [('hole'), ('hole', ['another', 'a'])]}, {'in': 1, 'action': 'abcdefg'}), None)
        self.assertIn('1', self.g.log[-1])
        self.assertIn('in', self.g.log[-1])
        self.assertIn('die', self.g.log[-1])
        self.assertIn('2', self.g.log[-1])
        #self.g.action({'action': ['die'], 'in': [('hole'), ('hole', ['another', 'a'])]}, {'subjobj': 1, 'action': 'abcdefg'})
        #self.assertIn('')
    
    def test_hashes(self):
        self.assertEqual(self.g.hash_check({'some crap': 'some more crap', 'action': 'abcdefg', 'action#throwable': 'throw! YEAH!'}, '#throwable'), 'throw! YEAH!')
        self.assertEqual(self.g.hash_check({'some crap': 'some more crap', 'action': 'abcdefg', 'action#throwable': 'throw! YEAH!'}, ''), 'abcdefg')
        self.assertEqual(self.g.hash_check({'some crap': 'some more crap', 'action': 'abcdefg', 'action#throwable': 'throw! YEAH!'}, '#throwable#yeetable'), 'throw! YEAH!')
        self.assertEqual(self.g.hash_check({'some crap': 'some more crap', 'action': '!@#$%', 'action#throwable': 'throw! YEAH!'}, '#meltable'), '!@#$%')
        self.assertEqual(self.g.hash_check({'some crap': 'some more crap', 'action': '12345', 'action#throwable': 'throw! YEAH!'}, ''), '12345')
        self.assertEqual(self.g.hash_check({'some crap': 'some more crap', 'action': 'abcdefg', 'action#throwable': 'throw! YEAH!'}, '#throwable'), 'throw! YEAH!')
        self.assertEqual(self.g.hash_check({'some crap': 'some more crap', 'action': 'abcdefg', 'action#throwable': 'throw! YEAH!', 'action#niceable': 'be super super COOOOOOOL!'}, '#throwable#niceable'), ['throw! YEAH!', 'be super super COOOOOOOL!'])
        self.assertEqual(self.g.hash_check({'some crap': 'some more crap', 'action': 'abcdefg', 'action#throwable': 'throw! YEAH!'}, '#throwable'), 'throw! YEAH!')
        self.assertEqual(self.g.hash_check({'some crap': 'some more crap', 'action': 'abcdefg', 'action#throwable': 'throw! YEAH!'}, ''), 'abcdefg')
        self.assertEqual(self.g.hash_check({'some crap': 'some more crap', 'action': 'abcdefg', 'action#throwable': 'throw! YEAH!'}, '#throwable#yeetable'), 'throw! YEAH!')
        self.assertEqual(self.g.hash_check({'some crap': 'some more crap', 'action': '!@#$%', 'action#throwable': 'throw! YEAH!'}, '#meltable'), '!@#$%')
        self.assertEqual(self.g.hash_check({'some crap': 'some more crap', 'action': '12345', 'action#throwable': 'throw! YEAH!'}, ''), '12345')
        self.assertEqual(self.g.hash_check({'some crap': 'some more crap', 'action': 'abcdefg', 'action#throwable': 'throw! YEAH!'}, '#throwable'), 'throw! YEAH!')
        self.assertEqual(self.g.hash_check({'some crap': 'some more crap', 'action': 'abcdefg', 'action#throwable#niceable': 'throw! YEAH!', 'action#niceable': 'be super super COOOOOOOL!'}, '#throwable#niceable'), 'throw! YEAH!')

    def test_hash_code(self):
        #TODO: finish writing this test
        self.assertEqual(self.g.hash_code({'action': ['hey']}, '0action ~ 01'), True)
        self.assertEqual(self.g.hash_code({'action': ['hey']}, '0action ~ 02'), False)
        self.assertEqual(self.g.hash_code({'action': ['hey']}, '0action ~ 01;0hi ~ 01'), None)
        self.assertEqual(self.g.hash_code({'action': ['hey'], 'hi': ['hi']}, '0action ~ 01;0hi ~ 01'), True)
        self.assertEqual(self.g.hash_code({'action': ['hey', 'hi'], 'words': ['hi']}, '0words ~ 01'), True)
        self.assertEqual(self.g.hash_code({'action': ['hey', 'hi'], 'words': ['hi', 'bye']}, '0words ~ 01'), False)
        self.assertEqual(self.g.hash_code({'action': ['hey', 'hi'], 'words': ['hi']}, '0words ~ 01;0action ~ 22'), True)
        self.assertEqual(self.g.hash_code({'action': ['hey', 'hi'], 'words': ['hi', 'bye']}, '0words ~ 11;0action ~ 510'), True)

if __name__ == '__main__':
    unittest.main()