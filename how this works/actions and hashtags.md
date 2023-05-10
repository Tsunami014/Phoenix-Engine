# this is how the actions work:

**PLEASE NOTE self.fc is the game**
self.fc contains every room and object

To check what elements of the sentence you need, run parsation.py

also note that if you want to specify a hashtag you need to create it if it does not exist, formula for doing so below.

# If you want to create a new action:

1. Add a blank dictionary with the key being the name of the action to actions.json
    example: `"smash": {}`
2. run parsation.py and input a sample sentence
3. find out what elements of that sentence you need
    example:


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
            key of the exit/object ('~' = all, '|' = delimener between multiple, [__] = delete_numbers[__])
    delimenar: '!!'
    fourth/fifth value with 5:
        what to set the value to (must be a python object)

else:
    Second value:
        with the set/change variables:
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
    Fourth digit (only for first number=7):
        0 = increase
        1 = decrease
        2 = set to
    Fourth number (only for first number=7):
        what number
```

# this is how the hashtags work:

```
first digit:
    0 - matching number of items
    1 - matching words

next text:
    the part of speech ('subjobj', 'action', 'what')
    
delimenar - " ~ "

for matching words:
    next text:
        the word to match (or series of words separated by " ~ ")

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

examples:
    - 0subjobj ~ 02 (checks if it has 2 subjobjs)
    - 0what ~ 54 (checks if there are less than 4 whats)
    - 1action ~ throw (checks that the action is throwing (throwing is in the list of actions))
    - 1subjobj ~ pot ~ pan ~ knife ~ jar (checks that the subjobjs contain a pot, pan, knife, or jar)```\