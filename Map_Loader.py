import json

data = json.load(open("Forest Map/The forest of wonder.json"))

rooms = {}

end_room = -1

for element in data['elements']:
    if element['_type'] == 'Room':
        room = {}
        room['name'] = element['_name']
        room['description'] = element['_description']
        room['dark'] = element['_dark']
        room['shape'] = element['_shape']
        room['exits'] = []
        
        if element['_endroom']: end_room = element['id']
        room['objects'] = []
        for obj in element['objects']:
            obj_data = {}
            obj_data['name'] = obj['_name']
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
            rooms[element['_dockStart']]['exits'].append((element['_startDir'], element['_dockEnd']))
        except:
            pass
        try:
            rooms[element['_dockEnd']]['exits'].append((element['_endDir'], element['_dockStart']))
        except:
            pass

map_data = {'card': {'title': data['title'], 'author': data['author'], 'description': data['description']}, 'rooms': rooms, 'startRoom': data['startRoom'], 'endRoom': end_room}

f = open("out.json", 'w')
f.write(json.dumps(map_data, indent=2))