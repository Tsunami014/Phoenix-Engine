# Assement Text adventure

> This is the TAS assessment task :)

    This game uses input/output in app.py using flask forms
    This game uses class variables to store game information
    This game has comments and files describing things
    This game uses if/elif/else loops to parse the input to find what the output should be
    This game uses dictionaries and lists when parsing the input to find what the output should be
    This game uses json files to store the map created on trizbort.io and parsed by my map parser to be very useful and stores everything about each room in it.
    Dictionaries and lists are also used to store information about the actions you can do and other things like that.

## If you don't understand what something does then poke around in the file directories bcos everything is a bit of a mess right now sry

## How to play?

- Run app.py
- Wait for it to load (some computers load faster than others)
- Once it says `debugger active! website avaliable on localhost:5000` or whatever then go to the website it says.
- If it doesn't work then check you have all of these:

    flask
    flask_bootstrap
    flask_wtf
    wtforms
    bootstrap-flask
    nltk

- if that still does not work try typing in terminal `python -m spacy download en_core_web_sm` ***THIS IS VERY IMPORTANT***

- Select a map
- Input your action into the box and press enter
- You can do any action you want! Try picking up stuff or moving and hitting monsters.
- If at any time you want to save/load your adventure choose your save slot and press save/load
- If you want to repeat an action you can press the back arrow and it will go back to your previous action *please note* it will show previous and possibly incorrect information if you go back to the previous page but when you press enter to submit the action it will correct it
- Certain Functions might be spefic so rember to read all of the instructions
- Don't get frustrated if you can't complete a puzzle don't worry as most of the time you will get it with a bit of patience.
- If you get into a battle than you need to read all of the stats of your enemies, but a reminder that you cannot leave the room during a battle
- this is a good game

## The rest of all this are some depricated to-do lists.

## To do list

| what is it            | status      | who?   | Description                                      |
| --------------------- | ----------- | ------ |------------------------------------------------- |
| Poster                | In Progress | ALL    | Read criteria                                    |
| finish inventory      | Done        | Max    | make the inventory accessable for the actions    |
| add in all functions  | IN PROGRESS | all    | make all the map-specific functions              |
| finish how this works | IN PROGRESS | M+R+V  | finish documenting how this all works            |
| finish saving/loading | CONSIDERING | Max    | make sure saving/loading is as good as possible  |
| work out the unitests | ...         | Max    | work out what to do with the unittests           |
| redo side.py          | DONE!       | Max    | redo side.py to make it more cleaner and simpler |
| character selection   | Considering | Riley  | Add more personalisation to game                 |
| Voicelines            | In progress | Henry  | Adds more fun to game                            |
| website aesthetics    | IN PROGRESS | Viggo  | make the website look beautiful.                 |
| Video Script          | In Progress | Riley  | Script for video                                 |
| Poster/ Game Slip     | Done!!!!!!! | Riley  | Help us have a better video                      |
| Naming the Game       | Done!!!!    | ALL!!  | Every good game needs a name                     |
| Replit Units          | Done!!!!    |ALL     | To know how to do da codes                       |
|finish how it works.md | IN progress |All     | Explain stuff                                    |
|amour snapping         | In progress | Riley  |                                                  |

# Actions to put in

| tag               | name       | Description                | synonyms (if any)         |
| ----------------- | ---------- | -------------------------- | -----------------------   |
| #moveable         | throw      | Throw an object            | yeet,chuck,toss,          |
| #inventory        | take       | put an object in inventory | grab,etc.                 |
| #smashable        | smash      | Smash an object            | break,shatter,crash       |
| #liftable         | lift       | Lift item                  | pickup,gather,hoist       |
| #playable         | play       | Play a game or do a puzzle | game,arcade,begin         |
| #sleepable        | sleep      | Able to sleep on           | rest,nap,liedown          |
| #breakable        | break      | Break an item              | tear,rip,cut,hit          |
| #moveable         | push       | Push an item or object     |  move                     |
| #catchable        | catch      | Catch an item or object    |                           |
| #snapable         | snap       | Snap an item or object     |                           |
| #consume          | consume    | eat an item and/or food    | eat,nom,bite,chomp        |
| #drink            | drink      | drink a potion/liquid      | consume,chug              |
| #burnable         | burn       | Burns stuff                | light up,flame,fire       |
| #purchasable      | purchase   | Purchase an item in shop   | buy                       |

## if you want something to happen not listed above then write what for below and i'll see to it

## **DO NOT PUT IN 'use'** as the WHOLE POINT of this is to make all different actions so you don't just say 'use' but have to specify what and make it more of a puzzle
