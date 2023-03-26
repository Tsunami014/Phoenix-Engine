print("Please bear with me as we do the imports...")
import spacy
import json
import tkinter.filedialog as fd

print("Now we're loading the map. Please choose a map to load from.")
data = json.loads(fd.askopenfile(filetypes=["JSON_file {json}"]).read().replace('\n', '/n'))

print("Now it's time to make the map work......")
nlp = spacy.load('en_core_web_sm')

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
        room['objects'] = []
        for obj in element['objects']:
            obj_data = {}
            if obj['_name'].find(" ") != -1:
                i = ' '
                tags = [tok.dep_ for tok in nlp(obj['_name'])]
                while i.find(" ") != -1:
                    i = obj['_name'].split(' ')[(tags.index("ROOT") if 'dobj' not in tags else tags.index("dobj")) if 'nsubj' not in tags else tags.index("nsubj")]
                    #i = input("The object with name '%s' has more than one word in its name.\n\
                    #Please input a one word name.\n> " % obj['_name'])
                obj_data['name'] = i
                obj_data['identifier'] = obj['_name']
            else:
                obj_data['name'] = obj['_name']
                obj_data['identifier'] = obj['_name']
            obj_data['description'] = obj['_description']
            obj_data['content'] = obj['_content']
            obj_data['type'] = obj['_kind']
            try:
                obj_data['status'] = obj['_status']
            except:
                obj_data['status'] = 0
            room['objects'].append(obj_data)
        rooms[element["id"]] = room
    if element['_type'] == 'Connector':
        try:
            rooms[element['_dockStart']]['exits'][round(element['_startDir'] / 2)] =  element['_dockEnd']
        except:
            pass
        try:
            rooms[element['_dockEnd']]['exits'][round(element['_endDir'] / 2)] = element['_dockStart']
        except:
            pass

map_data = {'card': {'title': data['title'], 'author': data['author'], 'description': data['description']}, 'rooms': rooms, 'actions': {}, 'startRoom': data['startRoom'], 'endRoom': end_room}
print("Now we're done! Please choose a file to output to.")
f = fd.asksaveasfilename(filetypes=["JSON_file {json}"])
if not f.endswith('.json'):
    f += '.json'
f = open(f, 'w')
f.write(json.dumps(map_data, indent=2))