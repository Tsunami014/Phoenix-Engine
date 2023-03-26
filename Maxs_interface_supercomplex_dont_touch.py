import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

print('importing... (please ignore the tensorflow "errors" unless it literally stops the application)')
from copy import deepcopy
import spacy
from nltk import Tree
from random import choice
from difflib import get_close_matches as GCM
import json

clear()
print('loading other vars ...')
ret = False
nlp = spacy.load('en_core_web_sm')
juiceless_tags = ['cc', 'det', 'aux']
cutoff = 0.85
#lemmatizer = WordNetLemmatizer() #doesn't work... yet
#These next vars are what to load from a file:
marker_tags = {'nsubj': 'subj', 'prep': '$$', 'advmod': '$$', 'pobj': 'obj', 'dobj': 'subjobj', 'xcomp': 'action'}
dollars_wrds = {'of': 'what', 'on': 'where'}
other_names = {'subjobj': 'name'}
actions = {("throw", 5): ['PYou throw the {0}{1}. It goes a little far before settling back down into the grass.', 'O("del ", "");PYou throw the {0}{1}. You accidentally throw it WAY too hard (tooootal accident) off into the sunset and now that {0} will never be seen again.']}
valid_actions = {("smash", 1): ['S2;Pyou smash {0}{1}. You get showered by the riches within!']}
"""For your information, the action and valid_action variables have a sort of code within them:
e.g.
S2;Pyou smash {0}{1}. Nothing happens.
look at the first character of each element in ___.split(';')
S: change the state(s) of the object(s) in question
P: print out the text
C: execute the code
O: execute: "%sfc['rooms'][str(room_id)]['objects'][object_id]%s" % (inp[0], inp[1])
example input for O:
"O('del ', '')" (which would evaluate to "del fc['rooms'][str(room_id)]['objects'][object_id]" which would delete the object)
"""

pos = ["north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest", "up", "down", "in", "out"]

with open("testing forest map.json") as f:
    fc = json.load(f)

clear()
print('loading functions...')

def run_action(code, object_id, room_id, values=[]):
    for act in code.split(';'):
        if act.startswith('S'):
            fc['rooms'][str(room_id)]['objects'][object_id]['status'] = act[1:]
        elif act.startswith('P'):
            print(act[1:].format(*values))
        #elif act.startswith('Q'):
        #    cur.execute(act[1:].format(*values))
        elif act.startswith('O'):
            exec("%sfc['rooms'][str(room_id)]['objects'][object_id]%s" % eval(act[1:]))
        else:
            exec(act[1:].format(*values))

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
            if tag[1] not in juiceless_tags:
                try:
                    m_t = marker_tags[tag[1]] #marker tag
                except:
                    print("couldn't find tag '%s' for word '%s' in dict." % (tag[1], tag[0].text))
                    continue
                if m_t == '$$':
                    m_t = dollars_wrds[GCM(tag[0].text, dollars_wrds.keys(), n=1, cutoff=cutoff)[0]]
                try:
                    out[m_t].append(tag[0])
                except:
                    out[m_t] = [tag[0]]
        else:
            tag = toks[wrds.index(i._label)]
            if tag[1] not in juiceless_tags:
                try:
                    m_t = marker_tags[tag[1]] #marker tag
                except:
                    print("couldn't find tag '%s' for word '%s' in dict." % (tag[1], tag[0].text))
                    continue
                end = p_t(i, toks, wrds)
                if m_t == '$$' and end != {}:
                    m_t = dollars_wrds[GCM(tag[0].text, dollars_wrds.keys(), n=1, cutoff=cutoff)[0]]
                    for i in end.keys():
                        try:
                            out[i+'#'+m_t].extend(end[i])
                        except:
                            out[i+'#'+m_t] = end[i]
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
    toks = [(tok, tok.dep_) for tok in doc]
    wrds = [str(tok) for tok in doc]

    global ret
    ret = False

    #specials = {""}
    #juiceless_wrds = []
    #for tok in toks:
    #    if tok[1] in juiceless_tags: juiceless_wrds.append(str(tok[0]))
    trees = [to_nltk_tree(sent.root) for sent in doc.sents]
    #print(toks)
    #for t in trees:
    #    try: print(t.pretty_print()+'\n')
    #    except: pass
    al = [i[0] for i in list(actions.keys())]
    #al.extend(specials.keys())
    for t in trees:
        try:
            closest = GCM(t._label.lower(), al, cutoff=cutoff, n=1)[0]
        except:
            print('Unknown command: %s. Avaliable commands: %s' % (t._label.lower(), str(al)))
            continue
        out = p_t(t, toks, wrds, t._label)
        print(out)
        
        try:
            out['subjobj']
        except:
            print('You need at least the object that you are doing something on!\nIf you did, consider rewording the sentence.\nYou said these objects: '+str(out['subjobj']))
            continue
        
        try:
            if out['subj'] not in ['i', 'me']:
                print("You can't get someone else to {0} a {1}".format(closest, out['subjobj']))
                continue
        except:
            pass
        
        if len(out['subjobj']) != 1:
            print('Too many/little objects specified. Please only specify one.\nIf you did, consider rewording the sentence.\nYou said these objects: '+str(out['subjobj']))
            continue # Director yells out, "NEXT!" while you are halfway in the middle of what you were showing them
        
        try:
            closest_obj = GCM(out['subjobj'][0].text.lower(), [i['name'].lower() for i in objs], cutoff=cutoff, n=1)[0]
        except:
            print('Unknown object: %s. Avaliable objects: %s' % (out['subjobj'][0].text.lower(), str([i['name'].lower() for i in objs])))
            continue
        
        obj_index = [i['name'].lower() for i in objs].index(closest_obj)
        
        try: # This uses its NAME to figure out what actions are allowed. If you want to do something different, change the 'closest_obj' in the statement below
            run_action(choice(valid_actions[(out['action'], closest_obj)]), obj_index, room_id, [closest, out['subjobj']])
        except: # This uses the TYPE of the object to figure out what actions are allowed. If you want to do something different, change the 'objs[[i['name'].lower() for i in objs].index(closest_obj)]['type']' (and also the lines after it)
            try:
                run_action(choice(actions[(closest, objs[[i['name'].lower() for i in objs].index(closest_obj)]['type'])]), obj_index, room_id, [closest, out['subjobj']])
            except:
                print('You can\'t %s an object of type %s!' % (closest, objs[[i['name'].lower() for i in objs].index(closest_obj)]['type']))
                continue
    return ret

clear()
print('"%s": by %s\n%s\nPress enter to start' % (fc['card']['title'], fc['card']['author'], fc['card']['description']))
input()
clear()

#roomnum = fc['startRoom']
roomnum = 1
describe = True

while True:
    croom = fc['rooms'][str(roomnum)]
    if describe:
      print("%s\n%s\n" % (croom['name'], croom['description']))
    print("It is%s dark.\nYou can %s\nThere are these objects: %s\nWhat do you do?" % ("" if croom['dark'] else "n't", 'not exit' if len(croom['exits']) == 0 else 'exit %s' % ", ".join(["%s towards %s" % (pos[round(i/2)], fc["rooms"][str(j)]["name"]) for i, j in croom['exits']]), [i['name'] for i in croom['objects']]))
    describe = parse(nlp(input()), roomnum, croom['objects'])