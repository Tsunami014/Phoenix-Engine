import random
import time
sword_in_stone_pullers={"name: Riley","name: Imzafish","name: Max","name: Viggo",}
#18 Rooms
#voicelines
#work in progress
def Voicelines():
  print('Vaules')
#Swap lock

#Pushing Boulder


#Character Choosing
character_choice=input("Choose a character")

#NPC Dialogue
if character_choice=="hi":
     print("filler")

#Quicksand
#The player needs to press the button and then do a quick reaction test to confirm they made it across.
if button_pressed==True:
     print("Get ready")
     time.sleep(1)
    
#Spinx code
print("Welcome Mortal solve this riddle to continue or DIE")
riddle_num=random.int(1,5)
if riddle_num==1:
    ans_riddle_1=input("Say my name and I disappear. What am I?")
    if ans_riddle_1=="Silence":
        print("Correct Answer, proceed")
    else :
        print("Wrong Answer")
        #Kill the player
elif riddle_num==2:
    ans_riddle_2=input("I run but never walk, have a mouth but never talk, have a bed but never sleep. What am I?")
    if ans_riddle_2.lower() =="river":
        print("Correct Answer, proceed")
    else:
        print("Wrong Answer")
        #Kill the player
elif riddle_num==3:
    ans_riddle_3=input("I am easy to lift, but hard to throw. What am I?")
    if ans_riddle_3==("A feather"):
        print("Correct Answer, proceed")
    else:
         print("Wrong Answer")
         #Kill the player
elif riddle_num==4:
    ans_riddle_5=input("The more you take, the more you leave behind. What am I?")
    if ans_riddle_5=="footsteps":
        print("Correct answer, proceed")
    else:
         print("Wrong Answer")
         #Kill the player
else:
    ans_riddle_5=input( "When you need me, you throw me away. When you’re done with me, you bring me back. What am I??")
    if ans_riddle_5==("Anchor"):
         print("Correct answer, proceed")
    else:
         print("Wrong Answer")
        #Kill the player

#funny lock
maze_finished=False
if maze_finished==True:
    print("You have finished the maze")
    time.sleep(1)
    print("A rustic old lock blocks your path")
    print("You attempt to lockpick the lock but fail however you decide to kick it instead")
    kick=input("Press K to continue")
    if kick=="K":
         print("You have successfully kicked the lock")
         print ("The door swings open")

#Defining the Enmies
#Mummies 25hp Attack Punch
#Swarm of Scorpians 45hp Attack Sting
#Snake 50hp Attack Bite


#boss fight
#have to kill two minions and the boss itself
#Pharoh's Guards 50hp each Attack Punch
#Pharoh  100hp   Attacl Staff of the Ra



#Sword in Stone 
Can_pull=True
chance_to_pull=random.randint(1,4)
if chance_to_pull==4:
     print("You are the almighty and have pulled the sword in the stone")
     name=input("You shall be recorded what is your name?(Please note your name will be recorded in the game)")
     sword_in_stone_pullers.update ({'name': name})
else:
     print("You have not pulled the sword in the stone")
     print("You cannot attempt to pull the sword in the stone again until you restart the game")
     Can_pull=False
     
#End of Map speficfic functions



#THIS CODE IS UNDER PROGRESS
#IT MAY NOT WORK 100%
#WHATEVER YOU DO TO THIS BELOW CODE PLEASE TELL ME
#IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#WHATEVER YOU DO TO THIS BELOW CODE PLEASE TELL ME

try:
    import connector as c
except ModuleNotFoundError:
    import Map_Specific_Functions.connector as c
from difflib import get_close_matches as GCM

from json import load
from random import randint, choice

#If at any time you want to stop the current action from being applied, then in the externals just pop in a "の" anywhere. It will get removed before being executed.

listener = c.EventListener()

#monsters dict in format: {name: [power (see below list powers for the number), hp]}
monsters = {'bokoblin': [0, 25], 'miniboss': [0, 30], 'lizard monster boss': [1, 40]} # change this
# and this v
#[(randeom number between 1 and this number, {if rolled this or below: 'code to execute', etc.})]
powers = [(10, {6:['tried to hit you... But it missed!', '... tried to hit you but you blocked!', 'hit your shield!'], 11: 'hit you for {5} HP!;71hp = 1{5}'}), (10, {4:['tried to hit you... But it missed!', '... tried to hit you but you blocked!', 'hit your shield!'], 7: 'hit you for {4} HP!;71hp = 1{4}', 11: 'hit you for {7} HP!!;71hp = 1{7}'})]

#{'name of object': [(roomnum, 'codewhenitactivates'), etc.], etc.}
room_connections = {'key': [(23, '6~!!5[0];5~!!426!!"6";00Your key opened the door of the house!')]} # and this if you need it

with open('important stuff/battles.json') as f:
    battle = load(f)

class Monster:
    def __init__(self, name: str, power: int=-1):
        self.name = name
        self.power = powers[power if power != -1 else monsters[name][0]]
        self.roll = self.power[0]
        self.power = self.power[1]
        self.hp = monsters[name][1]
    
    def __str__(self):
        return 'Monster <%s>' % (self.name)
    def __repr__(self):
        return 'Monster <%s>' % (self.name)
    
    def __hash__(self):
        return hash(id(self))
    
    def __eq__(self, other):
        return str(self) == str(other)
    
    def its_turn(self):
        value = randint(0, self.roll)
        for i in self.power.keys(): # for each number in the list of numbers:
            if i >= value: # if the value is closer to i than the last one (in the case of the first one, it must be less than 2 distance away)
                end = self.power[i] if type(self.power[i]) == str else choice(self.power[i])
                return '00The %s ' % self.name + end.format(*[str(randint(1, i+1)) for i in range(1, 12)]) # so you can go 'it hit you for {5} HP!' and that {5} will be replaced with a random number from 1 to 5
        return '00CODING ERROR: %s' % str(self)

@listener.wait(types=['init'])
def init(self):
    self.fight = False
    self.hp = 100
    self.inv = {}
    self.curmonsters = {}
    return ''

@listener.wait(types=['finish'])
def finish(self):
    if self.hp <= 0:
        return '00YOU DIED!!!;11redirect = "death"'
    for m in self.curmonsters:
        if m.hp <= 0:
            self.curmonsters.remove(m)
    if not self.curmonsters and self.fight:
        self.fight = False
        return '00YOU WON THE FIGHT!!!;4~!!4~'
    return ''

@listener.wait(types=['move']) # check each move to see if it sparks a fight
def wait_for_move(self):
    passageways = ''
    for i in room_connections:
        if i in self.inventory.keys() and room_connections[i][0] == self.roomnum:
            passageways += room_connections[i][1] + ';'
            
    tot = []
    rm = []
    for i in self.fc['rooms'][str(self.roomnum)]['objects']:
        l = GCM(i['identifier'], monsters.keys(), n=1, cutoff=self.cutoff)
        if l:
            tot.append(l[0])
            rm.append(i)
    for i in rm: self.fc['rooms'][str(self.roomnum)]['objects'].remove(i)
    if tot:
        self.fight = True
        self.curmonsters = [Monster(j) for j in tot]
        return passageways + '00OH NO! THERE IS A ' + " AND A ".join(tot) + r"! THEY START A FIGHT!!! (you can no longer exit);5~!!4~!!{}"#code to print and no longer exit
    return passageways

@listener.wait(types=['action'])
def action(self):
    # self.prev_action, ironically, is the current action and you can use said variable here!
    if self.fight:
        mt = turns(self)
        deps = None
        if self.prev_action in battle:
            for i in battle[self.prev_action]:
                if self.hash_code(self.p, i):
                    deps = battle[self.prev_action][i]
                    break
            if deps == None:
                deps = '00You cannot do that!' if 'else' not in battle[self.prev_action] else battle[self.prev_action]['else']
        if deps == None: skip = ''
        else: skip = 'の'
        if type(deps) == list:
            return ('%s%s%s%s' % (skip, mt, (';' if mt else ''), choice(deps).format(*[str(randint(1, i+1)) for i in range(1, 12)]))) # so you can go 'it hit you for {5} HP!' and that {5} will be replaced with a random number from 1 to 5
        elif deps == None:
            return ('%s%s' % (skip, mt))
        else:
            return ('%s%s%s%s' % (skip, mt, (';' if mt else ''), deps.format(*[str(randint(1, i+1)) for i in range(1, 12)]))) # so you can go 'it hit you for {5} HP!' and that {5} will be replaced with a random number from 1 to 5
    return ''

def turns(self):
    end = ';'
    for i in self.curmonsters:
        end += i.its_turn() + ';'
    return end[1:-1]





#Locks,Puzzles and traps are stored in this file so they are easy to read and edit.
import random
import time
import json


#Swap Lock can be modified to Work with Viggo's Music Lock
#Diffrent Colours Must be lined together. To work 
colour_options={"red","yellow","blue","green"}
empty_slots={"Empty,Empty"}
print(colour_options)
#Make the colour options assinable to a number or a slot
slot_1=random.choice(colour_options+empty_slots)
colour_options.remove(slot_1)
slot_2=random.choice(colour_options+empty_slots)
colour_options.remove(slot_2)
slot_3=random.choice(colour_options+empty_slots)
colour_options.remove(slot_3)
slot_4=random.choice(colour_options+empty_slots)
slot_5=random.choice(colour_options+empty_slots)






#This is code to order a set of Orbs or an Orb lock
# Don't forget this I have it above but will be needed normally; import random 
orb_lock_solved=False
number_clue=random.randint(1,3)
codeinput=["Red","yellow","blue","green"]
orbcode_options=["Red","yellow","blue","green"]
orbcode=random.shuffle(orbcode_options)
print(orbcode_options)
cluepart1=["In the center of the room stands an ornate fountain filled with water and four floating orbs - red, blue, yellow and green - each emitting its own unique light. Above them hangs a sign written in ancient runes which reads 'Order these Orbs'","A book shelf appears with multiple books but four catch your eye namely 'Blue Seas' by ; Joanna A, 'Murder Mysteries' by Callum Green, 'Red is the colour of Love' by Brigette L  and  'Postivity' by Peter Yellow","YA"]
if number_clue==1:
  orb1set_clue=cluepart1[0]
  print(orb1set_clue)
elif number_clue==2:
  orb2set_clue=cluepart1[1]
  print(orb2set_clue)
else:
  orb_last_set_clue=cluepart1[-1]
  print(orb_last_set_clue)
cluepart2=["What do you bury when it's alive and dig up when it's dead?","What's bought by the Yard but worn by the foot?"]


Solution_orb_text=["The Books rustle jumping around only for the books to splinter in a shower of paper, showing their true form as Orbs with four being coloured and the rest a mystical white." "The Orbs spin circling in a "]
#End of locks
#PUZZLE 1
import random

# Define some constants
NUM_DOORS = 4
NUM_SCARAB_SYMBOLS = 7
DOOR_SYMBOLS = ["☀️", "🔼", "*", "🌕"]
SCARAB_SYMBOLS = ["🔶", "🔵", "🟡", "🌕", "🌑", "🌊", "🌀"]
SCARAB_CENTER_INDEX = 3



# How the door puzzle works
#The room is a square with four doors, one on each wall, and each door is marked with a symbol. The walls are decorated with hieroglyphs, and a small pedestal sits in the center of the room with a single object on top. The object is a golden scarab beetle with a series of symbols carved into its back.

#Your task is to decipher the symbols on the scarab beetle and use that information to figure out which door to take in order to escape the room.

#Clues:

#The hieroglyphs on the walls depict a series of symbols that are similar to those on the scarab beetle.
#Each door is marked with a different symbol, but only one of them leads to the exit.
#The symbols on the scarab beetle are arranged in a circular pattern, with one symbol at the center and six others arranged around it.
#To solve the puzzle, you must do the following:

#Decipher the symbols on the scarab beetle by matching them to the hieroglyphs on the walls.
#Arrange the symbols in the correct order by starting with the central symbol and following the circular pattern.
#Use the resulting sequence of symbols to figure out which door to take by matching them to the symbols on the doors.
#For example, if the symbols on the scarab beetle are:

#[Central symbol] - [Symbol A] - [Symbol B] - [Symbol C] - [Symbol D] - [Symbol E] - [Symbol F]

#And the symbols on the doors are:

#Door 1: Symbol C
#Door 2: Symbol E
#Door 3: Symbol F
#Door 4: Symbol B
#Then you would take Door 4, since Symbol B is the second symbol in the sequence on the scarab beetle.




#PUZZLE 2


#The Mirror Puzzle is one of the Puzzles. The room contains a large mirror on one wall with hieroglyphs etched into its surface. Across the room, there is another wall with a series of hieroglyphs. The players must reflect a beam of light from a source (e.g., a crystal or a torch) onto a specific hieroglyph on the opposite wall.

#To do this, the players must use a series of levers and switches to manipulate the mirror and direct the beam of light towards the correct hieroglyph. Each lever or switch corresponds to a different angle or direction that the mirror can be adjusted, and the players must experiment with different combinations to find the correct angle to reflect the beam.

#However, if the players reflect the beam onto the wrong hieroglyph, a trap will be triggered, releasing poisonous gas into the room. The gas will quickly fill the room, making it difficult for the players to breathe and putting them in danger.

#To make the puzzle more challenging, the hieroglyphs on the opposite wall may be written in code or require a specific order to be solved. The players must decipher the clues and use their problem-solving skills to solve the Mirror Puzzle and move on to the next challenge



#To solve the Mirror Puzzle, the players need to follow these steps:

#Identify the hieroglyph that needs to be illuminated: The players must carefully study the wall with the hieroglyphs and determine which one needs to be illuminated. This could be indicated by a clue or a symbol in the room.

#Find the light source: The players need to locate the source of the beam of light. It could be a crystal, a torch, or some other object in the room.

#Adjust the levers and switches: The players must use the levers and switches to manipulate the mirror and direct the beam of light towards the correct hieroglyph. They can experiment with different combinations until they find the right angle to reflect the beam.

#Check the hieroglyph: Once the players believe they have reflected the beam of light onto the correct hieroglyph, they need to check it. They can do this by looking at the hieroglyph and verifying that it has been illuminated.

#Move on to the next challenge: If the correct hieroglyph has been illuminated, the players can move on to the next challenge. If not, they need to continue adjusting the mirror until they get it right.

#It's essential to be careful and deliberate when solving the Mirror Puzzle, as reflecting the beam of light onto the wrong hieroglyph will trigger the trap, releasing poisonous gas into the room.


#End of Puzzles for Ancient Egypt