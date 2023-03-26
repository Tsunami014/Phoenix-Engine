import side as s

s.debug = True
s.clear()
print('"%s": by %s\n%s\nPress enter to start' % (s.fc['card']['title'], s.fc['card']['author'], s.fc['card']['description']))
input()
s.clear()

#s.roomnum = s.fc['startRoom']
s.roomnum = 1

while True:
    croom = s.fc['rooms'][str(s.roomnum)]
    if s.title:
        s.clear()
        print(croom['name'].capitalize())
        print(croom['description'])
        s.title = False
    else:
        print()
    #5 = objects 6 = visible things 4 = actors
    if s.desc:
        #This prints "It isn't dark" if the room does not have the property 'dark' else it says it is dark.
        print("It is%s dark." % "" if croom['dark'] else "n't")
        
        #How this line works is it says you can not exit if there are no exits otherwise it states all the exits and the direction of exit.
        print("You can " + 'not exit' if len(croom['exits']) == 0 else ('exit ' + ", ".join(["%s towards %s" % (s.pos[int(i)], \
                s.fc["rooms"][str(croom['exits'][i])]["name"]) for i in croom['exits']])))
        
        #How these next 3 statements work: they basically make a string: "[item1, item2, item3]" for each item in the room's items that are of a certain type.
        print("There are these objects: " +         '['+"".join([i['identifier']+", " if i['type'] == 5 else '' for i in croom['objects']])+']')
        print("You can see: " +                     '['+"".join([i['identifier']+", " if i['type'] == 6 else '' for i in croom['objects']])+']')
        print("There are these people/monsters: " + '['+"".join([i['identifier']+", " if i['type'] == 4 else '' for i in croom['objects']])+']')
        
        print("What do you do?")
        if s.debug:
            #This lists all the debug statements you can make, but only if debug is activated.
            print("To debug: type \"DEBUG (type in one: %s) (parameters go here, type help if you are unsure)\"" % list(s.debug_actions.keys()))
            print("REMEMBER TO SAVE AFTER with \"save\"")
        s.desc = False
    print("Type in help to be helped.")
    i = input("\n> ")
    print()
    s.parse(s.nlp(i), s.roomnum, croom['objects'])