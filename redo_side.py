from copy import deepcopy
import json
import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

#Set some global variables
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
        
        self.output = [] #Instead of printing the output, return them in this list!

        #lemmatizer = WordNetLemmatizer() #doesn't work... yet

        #These next vars are what to load from a file:

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