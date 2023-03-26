import side as s

s.debug = True
s.clear()
print('"%s": by %s\n%s\nPress enter to start' % (s.fc['card']['title'], s.fc['card']['author'], s.fc['card']['description']))
input()
s.clear()

#roomnum = fc['startRoom']
s.roomnum = 1

while True:
    croom = s.fc['rooms'][str(s.roomnum)]
    if s.title:
        s.clear()
        print("%s\n%s\n" % (croom['name'].capitalize(), croom['description']))
        s.title = False
    else:
        print()
    #5 = objects 6 = visible things 4 = actors
    if s.desc:
        print("It is%s dark.\nYou can %s\nThere are these objects: %s\nYou can see %s\nThere are these people/monsters: %s\nWhat do you do?" % (\
            "" if croom['dark'] else "n't", \
            'not exit' if len(croom['exits']) == 0 else 'exit %s' % ", ".join(["%s towards %s" % (s.pos[int(i)], \
            s.fc["rooms"][str(croom['exits'][i])]["name"]) for i in croom['exits']]), \
            '['+"".join([i['identifier']+", " if i['type'] == 5 else '' for i in croom['objects']])+']', \
            '['+"".join([i['identifier']+", " if i['type'] == 6 else '' for i in croom['objects']])+']', \
            '['+"".join([i['identifier']+", " if i['type'] == 4 else '' for i in croom['objects']])+']'))
        if s.debug:
            print("To debug: type \"DEBUG (type in one: %s) (parameters go here, type help if you are unsure)\"\nREMEMBER TO SAVE AFTER with \"save\"" % list(s.debug_actions.keys()))
        s.desc = False
    print("Type in help to be helped.")
    i = input("\n> ")
    print()
    s.parse(s.nlp(i), s.roomnum, croom['objects'])