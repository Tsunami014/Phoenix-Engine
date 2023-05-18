# this is how the actions work

**PLEASE NOTE self.fc is the game**
self.fc contains every room and object

To check what elements of the sentence you need, run parsation.py

also note that if you want to specify a hashtag you need to create it if it does not exist, formula for doing so below.

## If you want to create a new action

1. Add a blank dictionary with the key being the name of the action to actions.json
    example: `"smash": {}` MAKE SURE THAT if the previous one has no comma put it in.

    ```json
    "smash": {}
    "lift": {}```
    ***does not work***, nor does ```json
    "smash": {},
    "lift": {},```
    it HAS to be ```json
    "smash": {},
    "lift": {}```

***notise the commas***
2. run parsation.py and input a sample sentence
3. find out what elements of that sentence you need
    example: 1 subjobj
4. put that in the dictionary; e.g. `"smash": {"subjobj": 1}`
5. then add in what would happen if you say that on a correct object by spaecifying a hash tag (you can have more than one)
    example: `"smash": {"subjobj": 1, "action#smashable": ""}`
6. (optional) add in an `action` tag as well by itself. (If you don't it will default to 'you cannot do that')
    example: `"smash": {"subjobj": 1, "action#smashable": "", "action": ""}`
7. Fill these in using the code below.
    (not very good) example: `"smash": {"subjobj": 1, "action#smashable": "00You smashed an object!", "action": "That is not applicable."}`
8. Create a hashtag for each new one that does not exist
    example: If you specify a #smashable but you invented that and that does not exist yet you need to create one in hashtags.json; do step 1, 2, and 3 before using the hashtag code below. This time instead of being a dictionary it is a string.
        example: ```json
    "takeable":
        "0subjobj ~ 01;1subjobj ~ stick ~ pot"

Other things to note:

- You can specify things happening at random chance by instead of writing the code as a string, write it as a list of all possible code strings.

```
First number:
    0 = print
    1 = set variable (if not exists then create variable)
    2 = delete variable
    3 = log an event
    4 = reset a part of self.fc (set it back to its default value)
    5 = set a part of self.fc (if not exists then create)
    6 = delete a part of self.fc
    7 = change a variable
    8 = run code ## THIS IS HIGHLY HIGHLY INADVISABLE ## NO ONE DO THIS EVER IF YOU SEE SOME CODE WITH THIS LEAVE IT THIS IS LAST RESORT ##

with 8:
    second text:
        what code to run

with 4/5/6:
    second number:
        room number ('~' for current room)
    delimenar: '!!'
    third digit:
        0 = name
        1 = description
        2 = darkness
        3 = shape
        4 = exits
        5 = objects
    fourth value:
        with exits/objects:
            key of the exit/object ('~' = all, '|' = delimener between multiple, [**] = delete_numbers[**], (**) = object in the current room with name **)
    delimenar: '!!'
    fourth/fifth value with 5:
        what to set the value to (must be a python object)

else:
    Second value:
        with the set/change to variables:
            0 = global
            1 = class
        with the print:
            what colour
        with the delete variables:
            0 = the object specified
        with the log an event:
            event (as a string that can be passed into eval func)

    Third string (not for first number=2 or 3):
        what variable name/what to print
    
    Delimeter: " = "
    
    Fourth number (only for first number=1):
        what value to set it to
            0 = the closest exit to what was said
            anything else: the value to set it to
    Fourth digit (only for first number=7):
        0 = increase
        1 = decrease
        2 = set to
    Fourth number (only for first number=7):
        what number
```

## this is how the hashtags work

```
first digit:
    0 - matching number of items
    1 - matching words
    2 - matching word one level down the tree
    3 - matching number of items one level down the tree
    4 - matching item name in inventory (matching the words)

next text (not for matching in inventory):
    the part of speech ('subjobj', 'action', 'what')

delimenar - " ~ "

for matching words:
    next text:
        the word to match (or series of words separated by " ~ ", you can specify pre-made lists by going '[**]' which will use all the elements in item_groups[**])

for # of items:
    next digit:
        0 - ==
        1 - !=
        2 - >=
        3 - <=
        4 - >
        5 - <

    next number:
        the number of items to check

for each level down the tree:
    delimenar - " ~ "
    the name of the next item down to check (so the thing to check is first then the rest)

examples:
    - 0subjobj ~ 02 (checks if it has 2 subjobjs)
    - 0what ~ 54 (checks if there are less than 4 whats)
    - 1action ~ throw (checks that the action is throwing (throwing is in the list of actions))
    - 1subjobj ~ pot ~ pan ~ knife ~ jar (checks that the subjobjs contain a pot, pan, knife, or jar)```
