print("Please bear with me as we do the imports...")
import json
import tkinter.filedialog as fd

try:
    import spacy
    nlp = spacy.load('en_core_web_sm')
except:
    import en_core_web_sm
    nlp = en_core_web_sm.load()

print("Now we're loading the map. Please choose a map to load from.")
data = json.loads(open(fd.askopenfilename(filetypes=["JSON_file {json}"]), encoding="utf8").read().replace('\n', '/n'))

print("Now it's time to make the map work......")

rooms = {}

end_room = -1

for element in data['elements']:
    if element['_type'] == 'Room':
        room = {}
        room['name'] = element['_name'].lower()
        room['description'] = element['_description']
        room['dark'] = element['_dark']
        room['shape'] = element['_shape']
        room['exits'] = {}
        
        if element['_endroom']: end_room = element['id']
        def clean_objs(objs):
            end = []
            for obj in objs:
                obj_data = {}
                obj['_name'] = obj['_name'].lower()
                if obj['_name'].find(" ") != -1:
                    i = ' '
                    tags = [tok.dep_ for tok in nlp(obj['_name'])]
                    tags2 = [tok.lower_ for tok in nlp(obj['_name'])]
                    while i.find(" ") != -1:
                        i = tags2[(tags.index("ROOT") if 'dobj' not in tags else tags.index("dobj")) if 'nsubj' not in tags else tags.index("nsubj")]
                        #i = input("The object with name '%s' has more than one word in its name.\n\
                        #Please input a one word name.\n> " % obj['_name'])
                    obj_data['name'] = i
                    obj_data['identifier'] = obj['_name']
                else:
                    obj_data['name'] = obj['_name']
                    obj_data['identifier'] = obj['_name']
                obj_data['description'] = obj['_description']
                obj_data['content'] = [] if obj['_content'] == [] else clean_objs(obj['_content'])
                obj_data['type'] = obj['_kind']
                end.append(obj_data)
            return end
        room['objects'] = clean_objs(element['objects'])
        rooms[element["id"]] = room
    if element['_type'] == 'Connector':
        g = lambda x: x // 2 if x < 17 else 8 + (x - 8)
        try:
            rooms[element['_dockStart']]['exits'][g(element['_startDir'])] =  element['_dockEnd']
        except:
            pass
        if element['_oneWay'] == False:
            try:
                rooms[element['_dockEnd']]['exits'][g(element['_endDir'])] = element['_dockStart']
            except:
                pass

map_data = {'card': {'title': data['title'], 'author': data['author'], 'description': data['description']}, 'rooms': rooms, 'actions': {}, 'startRoom': data['startRoom'], 'endRoom': end_room}
print("Now we're done! Please choose a file to output to.")
f = fd.asksaveasfilename(filetypes=["JSON_file {json}"])
if not f.endswith('.json'):
    f += '.json'
f = open(f, 'w')
f.write(json.dumps(map_data, indent=2))