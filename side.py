import json
import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

from nltk import Tree
from copy import deepcopy
from difflib import get_close_matches as GCM

import other.externals
import other.connector as c
listener = c.EventListener()

if True: #SET THIS TO TRUE if you downloaded en_core_web_sm using spacy install en_core_web_sm
    import spacy
    nlp = spacy.load('en_core_web_sm')
else: #SET THIS TO FALSE if you downloaded en_core_web_sm using the .whl file that you download from the internet
    import en_core_web_sm
    nlp = en_core_web_sm.load()

PRINTS = ''
PRINTS += 'loading functions and other global variables...\n'

cutoff = 0.85 #The cutoff for get closest matches (How close it needs to be for the match to work, 0=anything 1=same thing)

#Here are all the positions possible - notice sometimes there is "" between two items
#And that is because it gets the closest direction to the one inputted and it is by 2 spaces so
# [0, 2, 5] 1 would be close enough to 0, but 3 is too far away from 2 or 5
#So the gap is because it does not want that number to be close enough to the others
#That it will be counted as close enough to pass
pos = ["north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest", "", "up", "", "down", "", "left", "", "right", "", "in", "", "out"]
fourth_numbers = ["self.fc['rooms'][str(self.roomnum)]['exits'][str(closest_num([int(i) for i in self.fc['rooms'][str(self.roomnum)]['exits'].keys()], pos.index(self.p['move'][0][0])))]"]
delete_numbers = ["self.fc['rooms'][str(self.roomnum)]['objects'][[i['name'] for i in self.fc['rooms'][str(self.roomnum)]['objects']].index[self.p['subjobj'][0][0]]]"]

class Game:
    def __init__(self):
        global PRINTS
        PRINTS = ''
        PRINTS += 'loading other vars ...\n'
        
        self.cutoff = cutoff # for those of us who can't reach that far down - here you go :)
        self.p = {} #A filler... just in case worst comes to worst
        
        self.roomnum = 1 #This is the starting room id
        
        self.log = []

        #lemmatizer = WordNetLemmatizer() #doesn't work... yet

        fp = "important stuff/" #The filepath to the json files

        #Gets marker_tags, dollars_wrds, and other_names from words&tags.json
        with open(fp+"words&tags.json") as f:
            fc = json.load(f)
            
        self.marker_tags = fc['marker_tags']
        self.dollars_wrds = fc['dollars_wrds']
        self.other_names = fc['other_names']

        #Get actions, valid actions and action_deps from actions.json
        with open(fp+"actions.json") as f:
            fc = json.load(f)

        #Do a little formatting with the actions and valid actions
        self.actions = fc

        #Get all adjective and word and sentence_word (checked against all words in sentence) synonyms from syns.json and do some formatting with them
        with open(fp+"syns.json") as f:
            syns = json.load(f)

        self.syns = {}
        for i in syns:
            for j in syns[i]:
                self.syns[j] = i
        
        with open(fp+"hashtags.json") as f:
            self.hashtags = json.load(f)

        #Get the map from the file
        with open("maps/Forest out.json") as f:
            self.fc = json.load(f) #This is the game object which is a json object
            self.tosavefc = deepcopy(fc) #This is the game to save so that in debug mode
                    #If you change something it changes both so it can save the original

        self.prev_action = None #What the previous action specified was
        PRINTS = ''
    
    def to_tree(self, node):
        if len(list(node.children)) > 0:
            return {(node.orth_, node.dep_): [self.to_tree(child) for child in node.children]}
        else:
            return (node.orth_, node.dep_)
    
    def parse(self, t):
        #{['took', 'ROOT']: [['I', 'nsubj'], {['dog', 'dobj']: [['my', 'poss']]}, {['for', 'prep']: [{['walk', 'pobj']: [['a', 'det']]}]}]}
        
        if type(t) == str:
            return t
        elif type(t) == list:
            out = {}
            for i in t:
                if type(i) == dict:
                    for j in i:
                        m_t = self.parse(j)
                        if m_t == False: continue
                        m_t[1].append(self.parse(i[j]))
                        try:
                            out[m_t[0]].append(m_t[1])
                        except:
                            out[m_t[0]] = [m_t[1]]
                    continue
                
                end = self.parse(tuple(i) if type(i) == list else i)
                if end == False: continue
                if type(end) == list:
                    try:
                        out[end[0]].append(end[1])
                    except:
                        out[end[0]] = [end[1]]
                else:
                    raise TypeError("Unexpected type %s!!!!! (CODING EROR)" % type(end))
            return out
        elif type(t) == tuple:
            try:
                m_t = self.marker_tags[t[1]] #marker tag
            except:
                self.log.append("couldn't find tag '%s' for word '%s' in dict." % (t[1], t[0]))
                return False
            if m_t == '$$':
                try:
                    m_t = self.dollars_wrds[GCM(t[0], self.dollars_wrds.keys(), n=1, cutoff=cutoff)[0]]
                except:
                    self.log.append("Could not find word '%s' in dollars_wrds" % t[0])
            return [m_t, [t[0]]]
        elif type(t) == dict:
            out = {}
            for i in t:
                ks = self.parse(i)
                if type(ks) == dict: ks = ks.keys()
                ks = list(ks)
                
                out.update(self.parse(t[i]))
                try:
                    out[ks[0]].append(ks[1])
                except:
                    out[ks[0]] = [ks[1]]
            return out
        else:
            raise TypeError('What the hell is this type; "%s"?' % str(type(i)))
    
    def run_action(self, code): #TODO: make this even better than it is now
        #NOTE: here I am!
        """
        This runs an action as defined by the formula below.

        Args:
            code (str): the string code to run.
        
        The code:
        (split by ';', so '00Hello;01Goodbye' are 2 different statements both executed seperately)
        
        First number:
            0 = print
            1 = set variable (if not exists then create variable)
            2 = delete variable
            3 = log an event
            4 = reset a part of self.fc (set it back to its default value)
            5 = set a part of self.fc (if not exists then create)
            6 = delete a part of self.fc
        
        with 4/5/6:
            second number:
                room number ('~' for current room)
            delimenar: '!!'
            third digit:
                0 = name
                1 = description
                2 = darkness
                3 = shape
                4 = exits
                5 = objects
            fourth value:
                with exits/objects:
                    key of the exit/object ('~' = all, '|' = delimener between multiple)
            delimenar: '!!'
            fourth/fifth value with 5:
                what to set the value to (must be a python object)
        
        else:
            Second value:
                with the set variables:
                    0 = global
                    1 = class
                with the print:
                    what colour
                with the delete variables:
                    0 = the object specified
                with the log an event:
                    event (as a string that can be passed into eval func)
            
            Third string (not for first number=2 or 3):
                what variable name/what to print
            
            Delimeter: " = "
            
            Fourth number (only for first number=1):
                what value to set it to
                    0 = the closest exit to what was said
        """        
        global PRINTS
        for act in code.split(';'):
            if act == '':
                continue
            if act[0] == '0':
                #colour = act[1]
                PRINTS += act[2:].format() + '\n'
            elif act[0] == '1':
                try:
                    spl = act[2:].split(' = ')
                    front = ('globals()[\'%s\']' if act[1] == '0' else 'self.%s') % spl[0]
                    exec(front.format() + " = " + fourth_numbers[int(spl[1])].format())
                except Exception as e:
                    self.log.append(str(e))
            elif act[0] == '2':
                try:
                    exec('del '+delete_numbers[int(act[1])].format())
                except Exception as e:
                    self.log.append(str(e))
            elif act[0] == '3':
                self.run_action(listener.event(eval(act[1:]), self))
            elif act[0] in ['4', '5', '6']:
                spl = act[1:].split('!!')
                def run(i='~'):
                    c = 'self.fc["rooms"]["' + \
                        (spl[1] if spl[1][1] != '~' else str(self.roomnum)) + '"]["' + \
                        ["name", "description", "dark", "shape", "exits", "objects"][int(spl[1][0])] + \
                        '"]' + ('["%s"]' % i if spl[1][0] in ['4', '5'] and i != '~' else '')
                    if act[0] == '4':
                        c += ' = ' + c[7:]
                    elif act[0] == '5':
                        c += ' = '+spl[2]
                    else:
                        t = eval(c)
                        c += ' = '
                        if type(t) == str:
                            c += '""'
                        elif type(t) == list:
                            c += '[]'
                        elif type(t) == dict:
                            c += r'{}'
                        else:
                            c += 'None'
                    try:
                        exec(c)
                    except Exception as e:
                        self.log.append(str(e))
                if spl[1][1] == '~':
                    run()
                for i in spl[1][1:].split('|'):
                    run(i)
    def get_closest_matches(self, inp, matchAgainst):
        inp_words = inp.split()
        l = len(inp_words)
        match_words = matchAgainst.split()
        matches = []
        extra = 1
        for i in range(len(match_words)+l):
            amnt = 0
            for j in match_words[i:i+l+extra]:
                if GCM(j, inp_words, 1, cutoff):
                    amnt += 1
            if amnt >= l:
                match_words[i:i+l+extra]
                # inp = 'nice dog'
                #matchAgainst = 'my beautiful nice dog'
                #out = 'beautiful nice dog' --X
                # match_words[i:i+l+extra] = ['beautiful', 'nice', 'dog']
                #out = ['nice', 'dog']
                #matches.append(" ".join(out))
                #'beautiful' not in inp
                #THERE MIGHT BE WORDS IN THE MIDDLE which are not in the inp list but keep those
                #just get rid of the end/start words
        return matches
    
    def __call__(self, txt):
        global PRINTS
        PRINTS = ''
        """for i in self.syns.keys():
            m = self.get_closest_matches(i, txt)
            if len(m) != 0:
                for j in m:
                    txt = txt.replace(j, self.syns[i])""" #WAITING FOR FRIENDS TO FINISH CODE SO I CAN UNCOMMENT THIS
                    
        doc = nlp(txt)
        trees = [self.to_tree(sent.root) for sent in doc.sents]
        for t in trees:       
            if type(t) == tuple:
                if len(GCM(t[0], ['help'], cutoff=cutoff, n=1)) != 0:
                    global desc, title
                    title = True
                    desc = True
                    continue
                elif self.prev_action != None:
                    doc = nlp("%s %s" % (self.prev_action, t[0]))
                    t = [self.to_nltk_tree(sent.root) for sent in doc.sents][0]
                else:
                    self.log.append("Sorry, you need to specify an action.")
                    continue
                    
            self.p = self.parse(t)
            try:
                acts = self.actions[self.p['action'][-1][0]]
            except KeyError:
                self.log.append(self.p['action'][-1][0]+' is not in actions list')
                continue
            parseAction = self.hash_check(acts, self.p)
            if parseAction == False: continue
            #TODO: random chance of action
            self.run_action(parseAction)
        return PRINTS
    
    def hash_code(self, t, code): #NOTE: here are the hash codes
        """
        The hash codes are like this:
        each statement is split by a semi-colon;

        first digit:
            0 - matching number of items
            1 - matching words
        
        next text:
            the part of speech ('subjobj', 'action', 'what')
            
        delimenar - " ~ "
        
        for matching words:
            next text:
                the word to match (or series of words separated by " ~ ")
        
        for # of items:
            next digit:
                0 - ==
                1 - !=
                2 - >=
                3 - <=
                4 - >
                5 - <
            
            next number:
                the number of items to check
        
        examples:
            - 0subjobj ~ 02 (checks if it has 2 subjobjs)
            - 0what ~ 54 (checks if there are less than 4 whats)
            - 1action ~ throw (checks that the action is throwing (throwing is in the list of actions))
            - 1subjobj ~ pot ~ pan ~ knife ~ jar (checks that the subjobjs contain a pot, pan, knife, or jar)
        """
        for i in code.split(';'):
            if i[0] == '0':
                try:
                    spl = i[1:].split(' ~ ')
                    if eval(str(len(t[spl[0]])) + ' ' + ['==', '!=', '>=', '<=', '>', '<'][int(spl[1][0])] + ' ' + spl[1][1:]):
                        pass
                    else:
                        return False
                except Exception as e:
                    self.log.append('ERROR: %s' % str(e))
                    return
            elif i[0] == '1':
                try:
                    spl = i[1:].split(' ~ ')
                    if len(GCM(t[spl[0]][0][0], spl[1:], 1, cutoff)) != 1:
                        return False
                except Exception as e:
                    self.log.append('ERROR: %s' % str(e))
                    return
        return True

    def hash_check(self, inp, t):
        closest = (None, -1)
        for i in inp:
            if 'action' in i and i != 'action':
                j = i.split('#')[1:]
                l = [self.hash_code(t, self.hashtags[k]) for k in j]
                if all(l):
                    if closest[1] < len(l):
                        closest = (inp[i], len(l))
                    elif closest[1] == len(l):
                        if type(closest[0]) != list: closest = ([closest[0], inp[i]], closest[1])
                        else: closest.append(inp[i])
            elif i != 'action':
                try:
                    if not len(t[i]) == inp[i]:
                        self.log.append('You need %i %s(s) you are %sing, not %i!' % (inp[i], i, t['action'][-1][0], len(t[i])))
                        return False
                except:
                    self.log.append('You need at least %i %s(s) you are %sing!' % (inp[i], i, t['action'][-1][0]))
                    return False
        if closest[0] == None:
            try:
                return inp['action']
            except KeyError:
                return '00'
        return closest[0]

def closest_num(numbers, value):
    """
    Find the closest number in the list values to the number value

    Args:
        numbers ([int]): the list of numbers to search over to fi
        value (int): _description_
    
    Returns:
        int/None: the closest number, but if it is not found then it returns None
    """
    
    closesst = (2, None)
    for i in numbers:
        if abs(i-value) < closesst[0]:
            closesst = (abs(i-value), i)
    
    return closesst[1]


