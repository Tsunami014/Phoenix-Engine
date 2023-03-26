import os, re
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

debug = True #This is whether to include debug mode or not.
roomnum = -1

print('importing... (There may be some warnings, if so just ignore them)')
from copy import deepcopy
from nltk import Tree
from random import choice
from difflib import get_close_matches as GCM

if True:
    import spacy
    nlp = spacy.load('en_core_web_sm')
else:
    import en_core_web_sm
    nlp = en_core_web_sm.load()


import json

clear()
print('loading other vars ...')
cutoff = 0.85
#lemmatizer = WordNetLemmatizer() #doesn't work... yet
#These next vars are what to load from a file:

with open("words&tags.json") as f:
    fc = json.load(f)
    
marker_tags = fc['marker_tags']
dollars_wrds = fc['dollars_wrds']
other_names = fc['other_names']

with open("actions.json") as f:
    fc = json.load(f)

actions = fc['actions']
actions = {eval(i): actions[i] for i in actions}

valid_actions = fc['valid_actions']
valid_actions = {eval(i): valid_actions[i] for i in valid_actions}

action_deps = fc['action_dependencies']

with open("syns.json") as f:
    syns = json.load(f)

all_adj_syns = {}
for i in syns['adjs']:
    for j in syns['adjs'][i]:
        all_adj_syns[j] = i
        
all_wrd_syns = {}
for i in syns['words']:
    for j in syns['words'][i]:
        all_wrd_syns[j] = i

if debug:
    with open("debug_actions.json") as f:
        debug_actions = json.load(f)
else:
    debug_actions = {}

pos = ["north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest", "", "up", "", "down", "", "left", "", "right", "", "in", "", "out"]

with open("out.json") as f:
    fc = json.load(f)
    tosavefc = deepcopy(fc)

title = True
desc = True
prev_action = None

# TODO: in actions.json, in the valid_actions, instead of specifying the name specify a tag like '#throwable'

clear()
print('loading functions...')

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

def run_action(code, values, debug=False, set_values_3=True):
    """
    This runs an action as defined by the formula below.

    Args:
        code (str): the string code to run.
        values (list): This also follows a specific formula that is needed. See below.
    
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
    - "*G*" = globals()
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
        act = act.replace("*G*", "globals()")
        if debug: act = act.replace("*R*", "tosavefc['rooms']['"+str(roomnum)+"']").replace("*RMN*", "[tosavefc['rooms'][i]['name'] for i in tosavefc['rooms']]").replace("*RMS*", "[i for i in tosavefc['rooms']]")
        else: act = act.replace("*R*", "fc['rooms']['"+str(roomnum)+"']").replace("*RMN*", "[fc['rooms'][i]['name'] for i in fc['rooms']]").replace("*RMS*", "[i for i in fc['rooms']]")
        if act.startswith('S'):
            spla = act[1:].format(*values).split(" = ")
            fc['rooms'][str(roomnum)]['objects'][values[2][spla[0]]]['status'] = spla[1]
        elif act.startswith('P'):
            print(act[1:].format(*values))
        #elif act.startswith('Q'):
        #    cur.execute(act[1:].format(*values))
        elif act.startswith('O'):
            exec(("%sfc['rooms']['"+str(values[5])+"']['objects']%s") % eval(act[1:].format(*values)))
        else:
            exec(act[1:].format(*values))
    if debug: run_action(code, values, debug=False)

def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_

def p_t(tree, toks, wrds, root=None): #parse tree
    out = {}
    for i in tree:
        if type(i) == str:
            tag = toks[wrds.index(i)]
            #if tag[1] not in juiceless_tags:
            try:
                m_t = marker_tags[tag[1]] #marker tag
            except:
                print("couldn't find tag '%s' for word '%s' in dict." % (tag[1], tag[0].text))
                continue
            if m_t == '$$':
                try:
                    m_t = dollars_wrds[GCM(tag[0].text, dollars_wrds.keys(), n=1, cutoff=cutoff)[0]]
                except:
                    print("Could not find word '%s' in dollars_wrds" % tag[0].text)
            try:
                out[m_t].append(tag[0])
            except:
                out[m_t] = [tag[0]]
        else:
            tag = toks[wrds.index(i._label)]
            #if tag[1] not in juiceless_tags:
            try:
                m_t = marker_tags[tag[1]] #marker tag
            except:
                print("couldn't find tag '%s' for word '%s' in dict." % (tag[1], tag[0].text))
                continue
            end = p_t(i, toks, wrds)
            if m_t == '$$' and end != {}:
                try:
                    m_t = dollars_wrds[GCM(tag[0].text, dollars_wrds.keys(), n=1, cutoff=cutoff)[0]]
                    for i in end.keys():
                        try:
                            out[i+'#'+m_t].extend(end[i])
                        except:
                            out[i+'#'+m_t] = end[i]
                except:
                    print("Could not find word '%s' in dollars_wrds" % tag[0].text)
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

def parse(doc, room_id, objs):
    global prev_action
    toks = [(tok, tok.dep_) for tok in doc]
    wrds = [str(tok) for tok in doc]
    
    if debug:
        if len(GCM('save', [wrds[0]], cutoff=cutoff, n=1)) != 0:
            with open("out.json", "w") as f:
                f.write(json.dumps(tosavefc, indent=2))
            print("saved successfully! :)")
            return
        elif len(GCM('debug', [wrds[0]], cutoff=cutoff, n=1)) != 0:
            if len(GCM('help', [wrds[2]], cutoff=cutoff, n=1)) != 0:
                print(debug_actions[wrds[1]][1])
            else:
                try:
                    closest = GCM('debug', list(debug_actions.keys()), cutoff=cutoff, n=1)[0]
                except:
                    return
                try:
                    run_action(debug_actions[closest][0], wrds, True, False)
                except Exception as e:
                    print("ERROR:", e)
                    print(debug_actions[closest][1])
            return
    
    #juiceless_wrds = []
    #for tok in toks:
    #    if tok[1] in juiceless_tags: juiceless_wrds.append(str(tok[0]))
    trees = [to_nltk_tree(sent.root) for sent in doc.sents]
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
                t = [to_nltk_tree(sent.root) for sent in doc.sents][0]
            else:
                print("Sorry, you need to specify an action.")
                continue
        out = p_t(t, toks, wrds, t._label)
        print(out)
        
        al = [(i[0] if type(i) != str else i) for i in list(actions.keys())]
        alls = deepcopy(al)
        alls.extend(all_adj_syns.keys())
        try:
            closest = GCM(t._label.lower(), alls, cutoff=cutoff, n=1)[0]
        except:
            print('Unknown command: %s. Avaliable commands: %s\nKeep in mind similar words work too' % (t._label.lower(), str(al)))
            continue
        if closest in all_adj_syns:
            closest = all_adj_syns[closest]
        
        prev_action = closest
        
        try:
            if out['subj'] not in ['i', 'me']:
                print("You can't get someone else to {0} a {1}".format(closest, out['subjobj']))
                continue
        except:
            pass
        
        dep = action_deps[closest]
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
                print('You need at least the %s you are %sing!\nIf you did, consider rewording the sentence.' % (dep[tri][1], closest))
                stop = True
                break
            
            if len(outfind) != dep[tri][0]:
                print('Too many/little %ss specified. Please only specify %s.\nIf you did, consider rewording the sentence.\nYou said these %s: '+outfind % (dep[tri][1], str(dep[tri][0]), dep[tri][1]))
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
                for i in all_wrd_syns.keys():
                    if all_wrd_syns[i] in al_obj_names:
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
                                print('Unknown %s: %s.\nObjects that can be used in this situation: %s' % (dep[tri][1], tx.lower(), str(al_objs)))
                                stop = True
                                break
                    if match not in al_objs:
                        if match in outs:
                            closests.append(match)
                            idxs.append(None)
                        else:
                            closests.append(all_wrd_syns[match])
                            idxs.append(al_objs.index(all_wrd_syns[match]))
                    else:
                        closests.append(match)
                        idxs.append(al_objs.index(match))
                if stop: break
        if stop: continue
        
        for i in range(len(closests)):
            try:
                if closests[i] in all_wrd_syns:
                    closests[i] = all_wrd_syns[closests[i]]
            except:
                try:
                    if closests[i][0] in all_wrd_syns:
                        closests[i] = all_wrd_syns[closests[i][0]]
                    else:
                        closests[i] = closests[i][0]
                except:
                    pass
        
        vals = [out, closest, closests, None, idxs, room_id]
        
        try: # This uses its NAME to figure out what actions are allowed. If you want to do something different, change the [ERROR] in the statement below
            run_action(choice(valid_actions[(closest, tuple(closests))]), vals)
        except: #This uses NOTHING to figure out what to do. This is like a fail message for anything that isn't special.
            run_action(choice(actions[(closest)]), vals)