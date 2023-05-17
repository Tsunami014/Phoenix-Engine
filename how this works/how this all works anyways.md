### Explaining our Code

# How our Locks and Puzzles  work
Locks,Puzzles and traps are stored in this file so they are easy to read and edit.
# Swap Lock is a lock where iffrent Colours Must be lined together, To work they randomly jump around each time you hit the button A and B moves only one that is currently lined up with arrow

# This is code to order a set of Orbs or an Orb lock
 Don't forget this I have it above but will be needed normally; import random
orb_lock_solved=False
number_clue=random.randint(1,3)
codeinput=["Red","yellow","blue","green"]
orbcode_options=["Red","yellow","blue","green"]
orbcode=random.shuffle(orbcode_options)
print(orbcode_options)
cluepart1=["In the center of the room stands an ornate fountain filled with water and four floating orbs - red, blue, yellow and green - each emitting its own unique light. Above them hangs a sign written in ancient runes which reads 'Order these Orbs'","A book shelf appears with multiple books but four catch your eye namely 'Blue Seas' by ; Joanna A, 'Murder Mysteries' by Callum Green, 'Red is the colour of Love' by Brigette L  and  'Postivity' by Peter Yellow","YA"]
if number_clue==1:
  orb1set_clue=cluepart1[0]
  print(orb1set_clue)
elif number_clue==2:
  orb2set_clue=cluepart1[1]
  print(orb2set_clue)
else:
  orb_last_set_clue=cluepart1[-1]
  print(orb_last_set_clue)
cluepart2=["What do you bury when it's alive and dig up when it's dead?","What's bought by the Yard but worn by the foot?"]

Solution_orb_text=["The Books rustle jumping around only for the books to splinter in a shower of paper, showing their true form as Orbs with four being coloured and the rest a mystical white." "The Orbs spin circling in a "]
# End of Basic Locks which can be slightly modified to fit most other Locks

# Arcade lock
 A lock where you have to select the correct arcade game to solve it.
    game_played = input("There are multiple different arcade machines here... Tetris, Space Invaders, Portal and Pacman. Which do you play? > ")
    el_solved = False
    if game_played in ["Space Invaders", "space invaders", "Space invaders", "space Invaders"]:
        print("You play Space Invaders and hit the final level... The blood rushes to your head, your arms go tingly, and you drink a convenient bottle of GFuel muck! Then you beat the level. To be honest it was pretty easy.")
        print("You hear a blipping sound and fanfare comes from the arcade machine which now displays: You have beaten Space Invaders!")
        print("Maybe you should check the cafeteria...")
        el_solved = True
    elif game_played in ["Tetris", "tetris", "Portal", "portal", "Pacman", "pacman", "pac man", "Pac Man", "Pac man", "pac Man"]:
        print("You play " + game_played + ", and, somehow, you beat it! Nothing happened. What a waste of time.")
    else:
        print("That's NOT A GAME")

# end of locks
# PUZZLE 1
# How the door puzzle works
 The room is a square with four doors, one on each wall, and each door is marked with a symbol. The walls are decorated with hieroglyphs, and a small pedestal sits in the center of the room with a single object on top. The object is a golden scarab beetle with a series of symbols carved into its back.

 Your task is to decipher the symbols on the scarab beetle and use that information to figure out which door to take in order to escape the room.

Clues:

 The hieroglyphs on the walls depict a series of symbols that are similar to those on the scarab beetle.
 Each door is marked with a different symbol, but only one of them leads to the exit.
The symbols on the scarab beetle are arranged in a circular pattern, with one symbol at the center and six others arranged around it.
 To solve the puzzle, you must do the following:

 Decipher the symbols on the scarab beetle by matching them to the hieroglyphs on the walls.
 Arrange the symbols in the correct order by starting with the central symbol and following the circular pattern.
 Use the resulting sequence of symbols to figure out which door to take by matching them to the symbols on the doors.
 For example, if the symbols on the scarab beetle are:

 [Central symbol] - [Symbol A] - [Symbol B] - [Symbol C] - [Symbol D] - [Symbol E] - [Symbol F]

 And the symbols on the doors are:

 Door 1: Symbol C
 Door 2: Symbol E
 Door 3: Symbol F
 Door 4: Symbol B
 Then you would take Door 4, since Symbol B is the second symbol in the sequence on the scarab beetle.

# PUZZLE 2 Mirror Puzzle

 The Mirror Puzzle is one of the more complex challenges in the Puzzle Room. The room contains a large mirror on one wall with hieroglyphs etched into its surface. Across the room, there is another wall with a series of hieroglyphs. The players must reflect a beam of light from a source (e.g., a crystal or a torch) onto a specific hieroglyph on the opposite wall.

 To do this, the players must use a series of levers and switches to manipulate the mirror and direct the beam of light towards the correct hieroglyph. Each lever or switch corresponds to a different angle or direction that the mirror can be adjusted, and the players must experiment with different combinations to find the correct angle to reflect the beam.

 However, if the players reflect the beam onto the wrong hieroglyph, a trap will be triggered, releasing poisonous gas into the room. The gas will quickly fill the room, making it difficult for the players to breathe and putting them in danger.

 To make the puzzle more challenging, the hieroglyphs on the opposite wall may be written in code or require a specific order to be solved. The players must decipher the clues and use their problem-solving skills to solve the Mirror Puzzle and move on to the next challenge

 To solve the Mirror Puzzle, the players need to follow these steps:

 Identify the hieroglyph that needs to be illuminated: The players must carefully study the wall with the hieroglyphs and determine which one needs to be illuminated. This could be indicated by a clue or a symbol in the room.

 Find the light source: The players need to locate the source of the beam of light. It could be a crystal, a torch, or some other object in the room.

 Adjust the levers and switches: The players must use the levers and switches to manipulate the mirror and direct the beam of light towards the correct hieroglyph. They can experiment with different combinations until they find the right angle to reflect the beam.

 Check the hieroglyph: Once the players believe they have reflected the beam of light onto the correct hieroglyph, they need to check it. They can do this by looking at the hieroglyph and verifying that it has been illuminated.

 Move on to the next challenge: If the correct hieroglyph has been illuminated, the players can move on to the next challenge. If not, they need to continue adjusting the mirror until they get it right.

 It's essential to be careful and deliberate when solving the Mirror Puzzle, as reflecting the beam of light onto the wrong hieroglyph will trigger the trap, releasing poisonous gas into the room.

# Puzzle 3 Scale

 The players enter a dark chamber with a large stone scale in the center. The scale has two plates, each with different hieroglyphs engraved on them. The players notice that the scale is unbalanced, with one plate tilted downwards.
 The players examine the hieroglyphs on the plates and see that each symbol has a numerical value. They also notice that the scale has markings on each side, indicating the weight needed to balance it.

The players must quickly calculate which combination of hieroglyphs will balance the scale and place them on the plates. If they choose the wrong combination, the scale will tip, and snakes will fall...

 Once the players correctly balance the scale, the snakes retreat back into the ceiling, and a door opens, leading to the next chamber.

# End of Locks Puzzles and Traps.py

# This is how game.py works

## first we do the imports

this line is for importing the regular expressions used in the code and also for the line following

 import os, re 

this line is for clearing the screen. It is the only use of the os library. it basically sets the function 'clear' to clear the screen, so whenever you need to clear the screen you call "clear()"

    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    clear()

This is whether to include debug mode or not. Its default is true, but it gets set to false in files like main.py where you play the game, not debug it.

    debug = True 

more importing

    print('importing... (There may be some warnings, if so just ignore them)')

this line imports the copy module, used in later code. This deepcopy function basically creates duplicates of items, but without keeping the same references. This is used because of very complicated reasons.

    from copy import deepcopy

this imports the tree library from nltk, for turning the complicated spacy trees into the more simplified ones from the nltk library.

    from nltk import Tree

this imports the random choice library

    from random import choice

this imports a very handy function that makes it so that it checks for very tiny spelling errors. Comes in handy.

    from difflib import get_close_matches as GCM

this is for loading the files.

    import json

### SET THIS TO TRUE if you downloaded en_core_web_sm using spacy install en_core_web_sm

### SET THIS TO FALSE if you downloaded en_core_web_sm using the .whl file that you download from the internet

    if True:
        import spacy
        nlp = spacy.load('en_core_web_sm')
    else:
        import en_core_web_sm
        nlp = en_core_web_sm.load()

then it sets up the game by clearing the screen and setting some variables.

 clear()
 print('loading functions and other global variables...')

The cutoff is... the cutoff for get closest matches (How close it needs to be for the match to work, 0=anything 1=same thing)

 cutoff = 0.85

the next variable pos is all the positions possible - notice sometimes there is "" between two items

And that is because it gets the closest direction to the one inputted and it is by 2 spaces so

[0, 2, 5] 1 would be close enough to 0, but 3 is too far away from 2 or 5

So the gap is because it does not want that number to be close enough to the others

That it will be counted as close enough to pass

 pos = ["north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest", "", "up", "", "down", "", "left", "", "right", "", "in", "", "out"]

This is the fourth number and delete expressions. More on all this below.

 fourth_numbers = ["""
 try:
     self.fc['rooms']['{5}']['exits'][str(closest_num([int(i) for i in self.fc['rooms']['{5}']['exits'].keys()], pos.index('{3}')))]
     self.title = True
     self.desc = True
 except: pass"""]

  delete_numbers = ["self.fc['rooms']['{5}']['objects'][{4}[0]]"]

The main game class!

 class Game:
     def __init__(self):
         clear()
         print('loading other vars...')

set some variables, mostly self explanitory

         self.roomnum = 1 #This is the starting room id
         self.log = [] #Instead of printing errors, return them in this list!
         self.output = [] #Instead of printing the output, return them in this list
         #lemmatizer = WordNetLemmatizer() #doesn't work... yet

These next vars we load from a file:

         fp = "actions, words & syns/" #The filepath to all the json files

This gets the marker tags, dollas_wrds, etc. More on that in the \_\_call__ function.

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

This gets all the adjectives and stores them in variables.

The adjectives are basically words that can be substituted with other words. e.g. the all_adj_syns are all the adjective synonyms, and those basically are synonyms for adjectives (or the actions) like a synonym for throw is chuck.

word synonyms are just synonyms for words in a phrase like a synonym for stick is twig

sent_wrds are sentence word synonyms - basically unfiltered, literrally just replaces the words in the input string synonyms. For example, 'the' could also be 'da' ('the stick', 'da stick')

It also formats this so in the end the result dictionary is in the format: (this is an example)

    {
        'da': 'the',
        'le': 'the'
    }

Because it starts off like (again, example):

    {
        'the': ['da', 'le']
    }

so it takes all the keys in the dictionary, and then all the lists of synonyms and then combines them into one dictionary.

And this is the code:

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

This takes the map from the file and loads it.

One thing to notice is that the self.fc and self.tosavefc are the same - this is because when we change something in the gameplay we want to not change it in the actual file to do everything again, but if we change something in debug mode and we want to save that we change self.tosavefc.

         #Get the map from the file
         with open("maps/Forest out.json") as f:
             self.fc = json.load(f)
             self.tosavefc = deepcopy(fc)

and lastly a few more self explanitory actions

         self.title = True
         self.desc = True
         self.prev_action = None

this next function is the function to run the action.

This runs an action as defined by the formula below.

Args:
    code (str): the string code to run.
    values (list): This also follows a specific formula that is needed. See below.
    debug (optional, bool): Whether or not to apply the action to both the debug and normal or just normal. Defaults to False (just normal).
    set_values_3 (optional, bool): Whether or not to set the third value in the list values or to just leave it. Defaults to True (change it).

Values:

- out (dict): The parsed dictionary of the nlp parsed sentence.
- action (str): The action that is being done. For printing reasons.
- closests (list) - the words in the output that match the action in actions.json
- singular (str, but please leave this as None when inputting the list):
    This basically is closests[0] for those actions that only use one object
    So the print statement can be simpler. Will be overridden at the start of this code, so leave it as None.
- idxs (list) - the indexes of the words in the closests list in the room
- room_id (int) - the id of the current room. This is also the variable roomnum, but... still needed in this list.

UNLESS IF YOU WANT ANOTHER SET OF VALUES FOR THE ACTIONS THEN:

1. set_values_3=False
Then you should be fine :)

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

Delimeter: " ~ "

Fourth number (only for first number=1):
    what value to set it to
        0 = the closest exit to what was said

TODO: explain bit by bit what this does

 def run_action(self, code, values, debug=False, set_values_3=True):
         if set_values_3:
             try:
                values[3] = values[2][0]
            except:
                values[3] = []
        for act in code.split(';'):
            if act[0] == '0':
                #colour = act[1]
                self.output.append(act[2:].format(*values))
            elif act[0] == '1':
                spl = act[2:].split(' ~ ')
                front = ('globals()[\'%s\']' if act[1] == '0' else 'self.%s') % spl[0]
                
                exec(front.format(*values) + " = " + fourth_numbers[int(spl[1])].format(*values))
            elif act[0] == '2':
                exec('del '+delete_numbers[int(act[1])].format(*values))
                
                
        if debug: self.run_action(code, values, debug=False) #? Do we need this?

    def to_nltk_tree(self, node):
        if node.n_lefts + node.n_rights > 0:
            return Tree(node.orth_, [self.to_nltk_tree(child) for child in node.children])
        else:
            return node.orth_

TODO: explain this

    def p_t(self, tree, toks, wrds, root=None): #parse tree
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

TODO: explain this

    def __call__(self, inp, room_id, objs):
        doc = nlp(inp)
        wrds = [str(tok) for tok in doc]
        changed = False
        for i in range(len(wrds)):
            check = GCM(wrds[i], self.sent_wrd_syns.keys(), cutoff=cutoff, n=1)
            if len(check) != 0:
                wrds[i] = self.sent_wrd_syns[check[0]]
                changed = True
        if changed: doc = nlp(" ".join(wrds))
        toks = [(tok, tok.dep_) for tok in doc]
        wrds = [str(tok) for tok in doc]
        
        """if debug:
            if len(GCM('save', [wrds[0]], cutoff=cutoff, n=1)) != 0:
                with open("out.json", "w") as f:
                    f.write(json.dumps(self.tosavefc, indent=2))
                self.output.append("saved successfully! :)")
                return self.output, self.log
            elif len(GCM('debug', [wrds[0]], cutoff=cutoff, n=1)) != 0:
                if len(GCM('help', [wrds[2]], cutoff=cutoff, n=1)) != 0:
                    self.output.append(self.debug_actions[wrds[1]][1])
                else:
                    try:
                        closest = GCM('debug', list(self.debug_actions.keys()), cutoff=cutoff, n=1)[0]
                    except:
                        return self.output, self.log
                    try:
                        self.run_action(self.debug_actions[closest][0], wrds, True, False)
                    except Exception as e:
                        self.log.append("ERROR:", e)
                        self.log.append(self.debug_actions[closest][1])
                return self.output, self.log"""
        
        #juiceless_wrds = []
        #for tok in toks:
        #    if tok[1] in juiceless_tags: juiceless_wrds.append(str(tok[0]))
        trees = [self.to_nltk_tree(sent.root) for sent in doc.sents]
        #print(toks)
        #for t in trees:
        #    try: print(t.pretty_print()+'\n')
        #    except: pass
        for t in trees:
            if type(t) == str:
                if len(GCM(t, ['help'], cutoff=cutoff, n=1)) != 0:
                    global desc, title
                    title = True
                    desc = True
                    continue
                elif self.prev_action != None:
                    doc = nlp("%s %s" % (self.prev_action, t))
                    toks = [(tok, tok.dep_) for tok in doc]
                    wrds = [str(tok) for tok in doc]
                    t = [self.to_nltk_tree(sent.root) for sent in doc.sents][0]
                else:
                    self.log.append("Sorry, you need to specify an action.")
                    continue
            out = self.p_t(t, toks, wrds, t._label)
            self.log.append(out) #Re-comment this line if you want detailed logs
            
            al = [(i[0] if type(i) != str else i) for i in list(self.actions.keys())]
            alls = deepcopy(al)
            alls.extend(self.all_adj_syns.keys())
            try:
                closest = GCM(t._label.lower(), alls, cutoff=cutoff, n=1)[0]
            except:
                self.log.append('Unknown command: %s. Avaliable commands: %s\nKeep in mind similar words work too' % (t._label.lower(), str(al)))
                continue
            if closest in self.all_adj_syns:
                closest = self.all_adj_syns[closest]
            
            self.prev_action = closest
            
            try:
                if out['subj'] not in ['i', 'me']:
                    self.log.append("You can't get someone else to {0} a {1}".format(closest, out['subjobj']))
                    continue
            except:
                pass
            
            dep = self.action_deps[closest]
            closests = []
            idxs = []
            stop = False
            for tri in dep.keys():
                try:
                    find = re.findall(tri, str(list(out.keys())))[0]
                    if type(find) != str:
                        find = list(find)
                        #find = find[0]
                        
                        dels = []
                        for i in range(len(find)):
                            if find[i] == '': dels.append(i)
                        dels.reverse()
                        for i in dels:
                            del find[i]
                        outfind = []
                        for j in find: outfind.extend(out[j])
                    else:
                        outfind = out[find]
                    
                except:
                    find = []
                
                if len(find) == 0:
                    self.log.append('You need at least the %s you are %sing!\nIf you did, consider rewording the sentence.' % (dep[tri][1], closest))
                    stop = True
                    break
                
                if len(outfind) != dep[tri][0]:
                    self.log.append('Too many/little %ss specified. Please only specify %s.\nIf you did, consider rewording the sentence.\nYou said these %s: '+outfind % (dep[tri][1], str(dep[tri][0]), dep[tri][1]))
                    stop = True
                    break # Director yells out, "NEXT!" while you are halfway in the middle of what you were showing them
                
                if dep[tri][2] != []:
                    outs = []
                    for i in out.keys():
                        if i in dep[tri][2]: outs.append(out[i][0].text.lower())
                    al_objs = []
                    for i in objs:
                        if i['type'] in dep[tri][2]: al_objs.append(i['name'].lower())
                    al_obj_names = deepcopy(al_objs)
                    al_obj_names.extend(outs)
                    for i in self.all_wrd_syns.keys():
                        if self.all_wrd_syns[i] in al_obj_names:
                            al_obj_names.append(i)
                    
                    for f in outfind:
                        if type(f) == tuple:
                            tx = f[0].text
                            #f = deepcopy(f[1])
                        else:
                            tx = f.text
                        try:
                            match = GCM(out[tx][0].text.lower(), al_obj_names, cutoff=cutoff, n=1)[0]
                        except:
                            try:
                                match = GCM(tx.lower(), al_obj_names, cutoff=cutoff, n=1)[0]
                            except:
                                try:
                                    match = GCM(tri.lower(), al_obj_names, cutoff=cutoff, n=1)[0]
                                except:
                                    self.log.append('Unknown %s: %s.\nObjects that can be used in this situation: %s' % (dep[tri][1], tx.lower(), str(al_objs)))
                                    stop = True
                                    break
                        if match not in al_objs:
                            if match in outs:
                                closests.append(match)
                                idxs.append(None)
                            else:
                                closests.append(self.all_wrd_syns[match])
                                idxs.append(al_objs.index(self.all_wrd_syns[match]))
                        else:
                            closests.append(match)
                            idxs.append(al_objs.index(match))
                    if stop: break
            if stop: continue
            
            for i in range(len(closests)):
                try:
                    if closests[i] in self.all_wrd_syns:
                        closests[i] = self.all_wrd_syns[closests[i]]
                except:
                    try:
                        if closests[i][0] in self.all_wrd_syns:
                            closests[i] = self.all_wrd_syns[closests[i][0]]
                        else:
                            closests[i] = closests[i][0]
                    except:
                        pass
            
            vals = [out, closest, closests, None, idxs, room_id]
            
            try: # This uses its NAME to figure out what actions are allowed. If you want to do something different, change the [ERROR] in the statement below
                self.run_action(choice(self.valid_actions[(closest, tuple(closests))]), vals)
            except: #This uses NOTHING to figure out what to do. This is like a fail message for anything that isn't special.
                self.run_action(choice(self.actions[(closest)]), vals)
        return self.output, self.log

TODO: this
Find the closest number in the list values to the number value

Args:
    numbers ([int]): the list of numbers to search over to fi
    value (int): _description_

Returns:
    int/None: the closest number, but if it is not found then it returns None

    def closest_num(numbers, value):
        
        closesst = (2, None)
        for i in numbers:
            if abs(i-value) < closesst[0]:
                closesst = (abs(i-value), i)
        
        return closesst[1]
# End of Game.py
# Start of App.py
# This is the web app that uses game.py to run the game
Importing all of the required.

    import sys
    sys.dont_write_bytecode = True

    from flask import Flask, render_template, redirect, url_for
    from flask_bootstrap import Bootstrap5

    from flask_wtf import FlaskForm, CSRFProtect
    from wtforms import *
    from wtforms.validators import DataRequired, Length

    import pickle as pkl

    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = '/save slots'

    import secrets
    foo = secrets.token_urlsafe(16)
    app.secret_key = foo

Bootstrap-Flask requires this line

    bootstrap = Bootstrap5(app)
Flask-WTF requires this line

    csrf = CSRFProtect(app)

    import game as s
        g = s.Game()

with Flask-WTF, each web form is represented by a class
"Game" can change; "(FlaskForm)" cannot
see the route for "/" and "index.html" to see how this is used

    class Game(FlaskForm):
        inp = StringField('Input', validators=[DataRequired(), Length(1)], render_kw={'autofocus': True})
        submit = SubmitField('Submit')

class SaveForm(FlaskForm):
    myChoices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    slot = SelectField(u'Save slot', choices=myChoices, validators=[DataRequired()])
    save = SubmitField('Save')
    load = SubmitField('Load')
    back = SubmitField('Return to map selector')

class Selector(FlaskForm):
    myChoices = ['Forest out', 'hahahahahaAAAAA', 'making sure this works', 'by adding in more stuff'] #input SPECIFIC MAP NAMES HERE, MUST BE THE EXACT NAME OF THE MAP FILES IN THE 'maps/' FOLDER
    choice = SelectField(u'Field name', choices = myChoices, validators = [DataRequired()])
    submit = SubmitField('Submit')
    
def load_room_desc(g):
    croom = g.fc['rooms'][str(g.roomnum)]
    objs = g.all_non_inventory_items()
    out = ''
    out += "It is%s dark." % ("" if croom['dark'] else "n't") + '\n'
    
    #How this line works is it says you can not exit if there are no exits otherwise it states all the exits and the direction of exit.
    out += "You can " + ('not exit' if len(croom['exits']) == 0 else ('exit ' + ", ".join(["%s towards %s" % (s.pos[int(i)], \
            g.fc["rooms"][str(croom['exits'][i])]["name"]) for i in croom['exits']]))) + '\n'
    
    #How these next 3 statements work: they basically make a string: "[item1, item2, item3]" for each item in the room's items that are of a certain type.
    out += "You have in your inventory: " +      '['+", ".join(['%i %ss' % (g.inventory[i][0], i) for i in g.inventory.keys()])+']' + '\n'
    out += "There are these objects: " +         '['+", ".join([i['identifier'] for i in objs if i['type'] == 5])+']' + '\n'
    out += "There are these people/monsters: " + '['+", ".join([i['identifier'] for i in objs if i['type'] == 4])+']' + '\n'
    out += "You can see: " +                     '['+", ".join([i['identifier'] for i in objs if i['type'] == 6])+']' + '\n'
    return out

# all Flask routes below

@app.route('/', methods = ['GET', 'POST'])
def chooser():
    global g
    form = Selector()
    if form.validate_on_submit():
        name = form.choice.data
        g.redirect = ''
        return redirect("main/"+name+'/', 303)
    return render_template('selector.html', form=form)

@app.route('/main/<id>/', methods = ['GET', 'POST'])
def index(id):
    global g
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = Game()
    form2 = SaveForm()
    name = ""
    savemsg = ""
    g.log = []
    if form.submit.data and form.validate():
        name = g(form.inp.data)
        if g.redirect:
            r = redirect(url_for(g.redirect))
            return r
        form.inp.data = ''
    if (form2.back.data or form2.save.data or form2.load.data) and form2.validate():
        if form2.back.data:
            return redirect(url_for('chooser'))
        elif form2.save.data:
            with open('saves/%s.save' % form2.slot.data, 'wb+') as f:
                f.write(pkl.dumps(g))
                f.close()
                savemsg = 'SUCESSFULLY SAVED FILE!!'
        elif form2.load.data:
            try:
                with open('saves/%s.save' % form2.slot.data, 'rb') as f:
                    g = pkl.loads(f.read())
                    f.close()
                    savemsg = 'SUCESSFULLY LOADED FILE!!'
            except Exception as e:
                savemsg = 'UNABLE TO LOAD FILE BECAUSE: %s' % e
    croom = g.fc['rooms'][str(g.roomnum)]
    gameinfo = ' HP: %s\nMonster health: ' % str(g.hp)
    gameinfo += str({i.name: i.hp for i in g.curmonsters})
    return render_template('app.html', title=id, roomname=croom['name'].capitalize(), desc=croom['description'].strip(' \t\n'), bigdesc=load_room_desc(g).strip(' \t\n'), form=form, form2=form2, message=name.strip(' \t\n'), logs=str(g.log), savemsg=savemsg, gameinfo=gameinfo)

@app.route('/death')
def death():
    return render_template('death.html', error='You appeared to have fallen during your adventure. Your grave was just a stick, rising into the cold, unforgiving air. No one will be around to mourn for your death.')

# 3 routes to handle errors - they have templates too

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', error=e), 500

@app.errorhandler(400)
def internal_server_error(e):
    return render_template('400.html', error=e), 400

# keep this as is
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)