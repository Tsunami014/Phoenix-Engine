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