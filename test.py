#It tests can you not read the file name?
import unittest
import game as s
from json import loads
import re, ast
import Map_Specific_Functions.FOWExternals as ext
import Map_Specific_Functions.connector as c

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

"""class ExternalsTest(unittest.TestCase):
    l = c.EventListener()
    
    def CTG(self, names_of_objects): # Create Temporary Game
        temp = 'temporary game'
        temp.fc = {'rooms': {'1': {'objects': [{'name': i} for i in names_of_objects]}}}
        self.l.event('init', temp)
        return temp
    
    def test_battle(self):
        self.l.event('throw', self.CTG(['stick', 'bin']))"""

class SideTests(unittest.TestCase):
    g = s.Game()
    
    def test_closest_num(self):
        self.assertEqual(s.closest_num(list(range(10)), 2), 2) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(s.closest_num(list(range(0, 10, 2)), 6), 6) # [0, 2, 4, 6, 8] 
        self.assertEqual(s.closest_num(list(range(0, 10, 4)), 3), 4) # [0, 4, 8]
        self.assertEqual(s.closest_num(list(range(0, 10, 5)), 1), 0) # [0, 5]
        self.assertEqual(s.closest_num(list(range(0, 10, 5)), 3), None) # [0, 5]
        self.assertEqual(s.closest_num(list(range(0, 10, 5)), 4), 5) # [0, 5]
        
    #TODO: test self.g.parse_word
    
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
            #print(self.g.log)
            self.assertEqual(res, loads(test.replace("'", '"')))
    
    #test_action is no longer used, as the feature is depracated since the arrival of the hash tags
    
    def test_hashes(self):
        self.assertEqual(self.g.hash_check({'action': 'abcdefg', 'action#throwable': 'throw! YEAH!'}, {'subjobj': [['pot', {'is': [['the']]}]], 'action': [['throw']]}), 'throw! YEAH!')
        self.assertEqual(self.g.hash_check({'action': 'abcdefg', 'action#throwable': 'throw! YEAH!'}, {'subjobj': [['pot', {'is': [['the']]}], ['secondpot']], 'action': [['throw']]}), 'abcdefg')
        self.assertEqual(self.g.hash_check({'action': 'abcdefg', 'action#throwable': 'throw! YEAH!'}, {'subjobj': [['pot', {'is': [['the']]}]], 'canbeyeeted': [['True']], 'action': [['throw']]}), 'throw! YEAH!')
        self.assertEqual(self.g.hash_check({'action': '!@#$%', 'action#throwable': 'throw! YEAH!'}, {'meltedobjs': [['pot', {'is': [['the']]}]], 'action': [['throw']]}), '!@#$%')
        self.assertEqual(self.g.hash_check({'action': '12345', 'action#throwable': 'throw! YEAH!'}, {'subj': [['I']], 'action': [['throw']]}), '12345')
        self.assertEqual(self.g.hash_check({'action': 'abcdefg', 'action#throwable': 'throw! YEAH!'}, {'subjobj': [['pot', {'is': [['the']]}]], 'action': [['throw']]}), 'throw! YEAH!')
        #self.assertEqual(self.g.hash_check({'action': 'abcdefg', 'action#throwable': 'throw! YEAH!', 'action#niceable': 'be super super COOOOOOOL!'}, '#throwable#niceable'), ['throw! YEAH!', 'be super super COOOOOOOL!'])

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
    
    def test_GCM(self):
        self.assertEqual(self.g.get_closest_matches('nice brown', 'I LOOVE my  nice brown dogggo !!!!!!'), ['nice brown'])
        self.assertEqual(self.g.get_closest_matches('beautiful', 'beauutiful yellow doggos are best!'), ['beauutiful'])
        self.assertEqual(self.g.get_closest_matches('nice brown', 'beauutiful nice lovelly brown doggos are best!'), ['nice lovelly brown'])

if __name__ == '__main__':
    unittest.main()