import json
import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

from nltk import Tree
from copy import deepcopy
from difflib import get_close_matches as GCM

if True: #SET THIS TO TRUE if you downloaded en_core_web_sm using spacy install en_core_web_sm
    import spacy
    nlp = spacy.load('en_core_web_sm')
else: #SET THIS TO FALSE if you downloaded en_core_web_sm using the .whl file that you download from the internet
    import en_core_web_sm
    nlp = en_core_web_sm.load()

clear()
print('loading functions and other global variables...')

cutoff = 0.85 #The cutoff for get closest matches (How close it needs to be for the match to work, 0=anything 1=same thing)
    
#Here are all the positions possible - notice sometimes there is "" between two items
#And that is because it gets the closest direction to the one inputted and it is by 2 spaces so
# [0, 2, 5] 1 would be close enough to 0, but 3 is too far away from 2 or 5
#So the gap is because it does not want that number to be close enough to the others
#That it will be counted as close enough to pass
pos = ["north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest", "", "up", "", "down", "", "left", "", "right", "", "in", "", "out"]
fourth_numbers = ["""
try:
    self.fc['rooms']['{5}']['exits'][str(closest_num([int(i) for i in self.fc['rooms']['{5}']['exits'].keys()], pos.index('{3}')))]
    self.title = True
    self.desc = True
except: pass"""]
delete_numbers = ["self.fc['rooms']['{5}']['objects'][{4}[0]]"]

class Game:
    def __init__(self):
        clear()
        print('loading other vars ...')
        
        self.roomnum = 1 #This is the starting room id
        
        self.log = []

        #lemmatizer = WordNetLemmatizer() #doesn't work... yet

        fp = "actions, words & syns/" #The filepath to the json files

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

        #Get the map from the file
        with open("maps/Forest out.json") as f:
            self.fc = json.load(f) #This is the game object which is a json object
            self.tosavefc = deepcopy(fc) #This is the game to save so that in debug mode
                    #If you change something it changes both so it can save the original

        self.prev_action = None #What the previous action specified was
    
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
                    out[ks[0]].append((i[0]))
                except:
                    out[ks[0]] = [ks[1]]
            return out
        else:
            raise TypeError('What the hell is this type; "%s"?' % str(type(i)))
    
    def action(self, action, match):
        found = None
        for i in match:
            if 'action' not in i and 'hash' not in i:
                try:
                    if len(action[i]) == match[i]:
                        found = match['action']
                    else:
                        self.log.append('You need %i %s(s) you are %sing, not %i!' % (match[i], i, action['action'], len(action[i])))
                except:
                    self.log.append('You need at least %i %s(s) you are %sing!' % (match[i], i, action['action']))
        return found
    
    def run_action(self, code): #TODO: make this even better than it is now
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
        
        Delimeter: " = "
        
        Fourth number (only for first number=1):
            what value to set it to
                0 = the closest exit to what was said
        """
        for act in code.split(';'):
            if act[0] == '0':
                #colour = act[1]
                self.log.append(act[2:].format())
            elif act[0] == '1':
                spl = act[2:].split(' = ')
                front = ('globals()[\'%s\']' if act[1] == '0' else 'self.%s') % spl[0]
                
                exec(front.format() + " = " + fourth_numbers[int(spl[1])].format())
            elif act[0] == '2':
                exec('del '+delete_numbers[int(act[1])].format())
    
    def get_closest_matches(self, inp, matchAgainst):
        #I CHOOSE YOU! RILEY/VIGGO! I'M DESIGNATING THIS TIME!!!!!!!! HAHAHAHA!!!!!
        #What I want this function to do is this:
        #Let's say we have a phrase, matchAgainst. I want to use a GCM function to find if inp is in the phrase.
        #One hint is that you can use a sliding approach;
        #E.g. if the inp is 3 words long check each 3 words to see if they have the match
        #It is optional but nicer if you haev it so that you can have a word in the middle,
        #like if you have the inp='nice doggo' and matchAgainst='nice brown doggo' it will count as a match
        #If there is more than 1 then return them in a list
        #The really easy way to find out if this code works is to NOT RUN IT but run the test in test.py
        #Either by running the individual test or the whole file it makes no difference
        pass
    
    def __call__(self, txt):
        for i in self.syns.keys():
            m = self.get_closest_matches(i, txt)
            if len(m) != 0:
                for j in m:
                    txt = txt.replace(j, self.syns[i])
                    
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
                    
            p = self.parse(t)
            parseAction = self.hash_check(p['action'][0][0], '') #TODO: finish this
            try:
                act = GCM(parseAction[0][0], self.actions.keys(), 1, cutoff)[0]
            except:
                self.log.append('Sorry, but you cannot %s.' % p['action'][0][0])
                continue
            #TODO: random chance of action
            code = self.action(p, self.actions[act])
            if code == None: continue
            self.run_action(code)
    
    def hash_code(self, t, code):
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
                the word to match
        
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
        """
        found = []
        for i in code.split(';'):
            if i[0] == '0':
                pass
            elif i[0] == '1':
                try:
                    spl = i[1:].split(' ~ ')
                    if len(GCM(spl[1], [t[spl[0]]], 1, cutoff)) == 1:
                        found.append(())
                    else:
                        continue
                except Exception as e:
                    self.log('ERROR: %s' % str(e))
                    continue
                try:
                    if len(action[i]) == match[i]:
                        found = match['action']
                    else:
                        self.log.append('You need %i %s(s) you are %sing, not %i!' % (match[i], i, action['action'], len(action[i])))
                except:
                    self.log.append('You need at least %i %s(s) you are %sing!' % (match[i], i, action['action']))
        return found

    def hash_check(self, inp, hashtags):
        hashtags = hashtags.split('#')[1:]
        closest = (None, -1)
        for i in inp:
            if 'action' in i and i != 'action':
                j = i.split('#')[1:]
                l = [k in hashtags for k in j]
                if all(l):
                    if closest[1] < len(l):
                        closest = (inp[i], len(l))
                    elif closest[1] == len(l):
                        if type(closest[0]) != list: closest = ([closest[0], inp[i]], closest[1])
                        else: closest.append(inp[i])
        if closest[0] == None: return inp['action']
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