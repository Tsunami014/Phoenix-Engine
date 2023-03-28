import os, re
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

debug = True #This is whether to include debug mode or not.

print('importing... (There may be some warnings, if so just ignore them)')
#Import the nececary libraries
from copy import deepcopy
from nltk import Tree
from random import choice
from difflib import get_close_matches as GCM
import json

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

class Game:
    def __init__(self):
        clear()
        print('loading other vars ...')
        
        self.roomnum = 1 #This is the starting room id
        
        self.log = [] #Instead of printing errors, return them in this list!
        
        self.output = [] #Instead of printing the output, return them in this list

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

        #If it is in debug mode then get debug_actions from debug_actions.json else just leave it blank
        if debug:
            with open(fp+"debug_actions.json") as f:
                self.debug_actions = json.load(f)
        else:
            self.debug_actions = {}

        #Get the map from the file
        with open("maps/Forest out.json") as f:
            self.fc = json.load(f) #This is the game object which is a javascript object
            self.tosavefc = deepcopy(fc) #This is the game to save so that in debug mode
                    #If you change something it changes both so it can save the original

        self.title = True #Whether to show the title
        self.desc = True #Whether to show the description
        self.prev_action = None #What the previous action specified was

    def run_action(self, code, values, debug=False, set_values_3=True):
        """
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
        2. don't use S to change the state
        Then you should be fine :)
        
        The code:
        e.g.
        S0 = 2;Pyou smash {0}{1}. Nothing happens.
        look at the first character of each element in ___.split(';') (in this case, S and P)
        
        S: change the state of the object in question. 
        Basically, fc['rooms'][str(roomnum)]['objects'][_____]['status'] = ______
        In this case, because the code was "S0 = 2;", the object at 0 would have its state changed to 2.
        P: print out the text
        C: execute the code
        O: execute: "%sfc['rooms'][str(room_id)]['objects']%s" % (_____, ______)
        example input for O:
        "O('del ', '[0]')" (which would evaluate to "del fc['rooms'][str(room_id)]['objects'][object_id][0]" which would delete the object)
        
        Timesavers:
        - "*S*" = self.
        - "*R*" = fc['rooms']['"+roomnum+"']
        - "*RMN*" = [fc['rooms'][i]['name'] for i in fc['rooms']]
        - "*RMS*" = [i for i in fc['rooms']]
        """
        if set_values_3:
            try:
                values[3] = values[2][0]
            except:
                values[3] = []
        for act in code.split(';'):
            act = act.replace("*S*", "self.")
            if debug: act = act.replace("*R*", "self.tosavefc['rooms']['"+str(self.roomnum)+"']").replace("*RMN*", "[self.tosavefc['rooms'][i]['name'] for i in self.tosavefc['rooms']]").replace("*RMS*", "[i for i in self.tosavefc['rooms']]")
            else: act = act.replace("*R*", "self.fc['rooms']['"+str(self.roomnum)+"']").replace("*RMN*", "[self.fc['rooms'][i]['name'] for i in self.fc['rooms']]").replace("*RMS*", "[i for i in self.fc['rooms']]")
            if act.startswith('S'):
                spla = act[1:].format(*values).split(" = ")
                self.fc['rooms'][str(self.roomnum)]['objects'][values[2][spla[0]]]['status'] = spla[1]
            elif act.startswith('P'):
                self.output.append(act[1:].format(*values))
            #elif act.startswith('Q'):
            #    cur.execute(act[1:].format(*values))
            elif act.startswith('O'):
                exec(("%sself.fc['rooms']['"+str(values[5])+"']['objects']%s") % eval(act[1:].format(*values)))
            else:
                exec(act[1:].format(*values))
        if debug: self.run_action(code, values, debug=False)

    def to_nltk_tree(self, node):
        if node.n_lefts + node.n_rights > 0:
            return Tree(node.orth_, [self.to_nltk_tree(child) for child in node.children])
        else:
            return node.orth_

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
        global prev_action
        toks = [(tok, tok.dep_) for tok in doc]
        wrds = [str(tok) for tok in doc]
        
        if debug:
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
                return self.output, self.log
        
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
                elif prev_action != None:
                    doc = nlp("%s %s" % (prev_action, t))
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
            
            prev_action = closest
            
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
                    #TODO: add synonyms for the above
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