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
        
        self.output = []

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
        self.actions = fc['actions']
        self.actions = {eval(i): self.actions[i] for i in self.actions}

        self.valid_actions = fc['valid_actions']
        self.valid_actions = {eval(i): self.valid_actions[i] for i in self.valid_actions}

        self.action_deps = fc['action_dependencies']

        #Get all adjective and word and sentence_word (checked against all words in sentence) synonyms from syns.json and do some formatting with them
        with open(fp+"syns.json") as f:
            syns = json.load(f)

        self.all_adj_syns = {}
        for i in syns['adjs']:
            for j in syns['adjs'][i]:
                self.all_adj_syns[j] = i
                
        self.all_wrd_syns = {}
        for i in syns['words']:
            for j in syns['words'][i]:
                self.all_wrd_syns[j] = i
        
        self.sent_wrd_syns = {}
        for i in syns['sent_wrds']:
            for j in syns['sent_wrds'][i]:
                self.sent_wrd_syns[j] = i

        #Get the map from the file
        with open("maps/Forest out.json") as f:
            self.fc = json.load(f) #This is the game object which is a json object
            self.tosavefc = deepcopy(fc) #This is the game to save so that in debug mode
                    #If you change something it changes both so it can save the original

        self.prev_action = None #What the previous action specified was
    
    def to_nltk_tree(self, node):
        if node.n_lefts + node.n_rights > 0:
            return Tree(node.orth_, [self.to_nltk_tree(child) for child in node.children])
        else:
            return node.orth_
    
    def parse(self, tree, toks, wrds, root=None): #parse tree
        self.output = []
        self.log = []
        out = {}
        for i in tree:
            if type(i) == str:
                tag = toks[wrds.index(i)]
                #if tag[1] not in juiceless_tags:
                try:
                    m_t = self.marker_tags[tag[1]] #marker tag
                except:
                    self.log.append("couldn't find tag '%s' for word '%s' in dict." % (tag[1], tag[0].text))
                    continue
                if m_t == '$$':
                    try:
                        m_t = self.dollars_wrds[GCM(tag[0].text, self.dollars_wrds.keys(), n=1, cutoff=cutoff)[0]]
                    except:
                        self.log.append("Could not find word '%s' in dollars_wrds" % tag[0].text)
                try:
                    out[m_t].append(tag[0])
                except:
                    out[m_t] = [tag[0]]
            else:
                tag = toks[wrds.index(i._label)]
                #if tag[1] not in juiceless_tags:
                try:
                    m_t = self.marker_tags[tag[1]] #marker tag
                except:
                    self.log.append("couldn't find tag '%s' for word '%s' in dict." % (tag[1], tag[0].text))
                    continue
                end = self.p_t(i, toks, wrds)
                if m_t == '$$' and end != {}:
                    try:
                        m_t = self.dollars_wrds[GCM(tag[0].text, self.dollars_wrds.keys(), n=1, cutoff=cutoff)[0]]
                        for i in end.keys():
                            try:
                                out[i+'#'+m_t].extend(end[i])
                            except:
                                out[i+'#'+m_t] = end[i]
                    except:
                        self.log.append("Could not find word '%s' in dollars_wrds" % tag[0].text)
                else:
                    if end == {}:
                        try:
                            out[m_t].append(tag[0])
                        except:
                            out[m_t] = [tag[0]]
                    else:
                        try:
                            out[m_t].append((tag[0], end))
                        except:
                            out[m_t] = [(tag[0], end)]
        if root != None:
            try:
                out['action'].append(root)
            except:
                out['action'] = root
        return out

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