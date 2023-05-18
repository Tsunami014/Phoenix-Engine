#Forrst of Wonder externals
try:
    import connector as c
except ModuleNotFoundError:
    import Map_Specific_Functions.connector as c
from difflib import get_close_matches as GCM

from json import load
from random import randint, choice

#If at any time you want to stop the current action from being applied, then in the externals just pop in a "の" anywhere. It will get removed before being executed.

listener = c.EventListener('FOWExternals')

#monsters dict in format: {name: [power (see below list powers for the number), hp]}
monsters = {'bokoblin': [0, 25], 'miniboss': [0, 30], 'lizard monster boss': [1, 40]}
powers = [(10, {6:['tried to hit you... But it missed!', '... tried to hit you but you blocked!', 'hit your shield!'], 11: 'hit you for {5} HP!;71hp = 1{5}'}), (10, {4:['tried to hit you... But it missed!', '... tried to hit you but you blocked!', 'hit your shield!'], 7: 'hit you for {4} HP!;71hp = 1{4}', 11: 'hit you for {7} HP!!;71hp = 1{7}'})]

#{'name of object': [(roomnum, 'codewhenitactivates'), etc.], etc.}
room_connections = {'key': [(23, '6~!!5(key);5~!!46!!26;00Your key opened the door of the house!')]}

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
    passageways = ''
    for i in room_connections:
        if i in self.inventory.keys() and room_connections[i][0][0] == self.roomnum:
            passageways += room_connections[i][0][1] + ';'
    return passageways

@listener.wait(types=['move']) # check each move to see if it sparks a fight
def wait_for_move(self):
    autopickups = ''
    if self.roomnum == 17:
        for i in self.fc['rooms'][str(self.roomnum)]['objects']:
            if i['name'] == 'jeremy':
                autopickups += '00Jeremy decides to come with you!;6~!!5%i;11inventory["Jeremy"] = (1, \{"name": "jeremy", "identifier": "jeremy", "type": 4\});' % self.fc['rooms'][str(self.roomnum)]['objects'].index(i)
                break
    
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
        return autopickups + '00OH NO! THERE IS A ' + " AND A ".join(tot) + r"! THEY START A FIGHT!!! (you can no longer exit);5~!!4~!!{}"#code to print and no longer exit
    return autopickups

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

#by the way the rest of these are for show and do not actually do stuff yet
#please note these (below) are examples of events, and are not actual events.
"""
@listener.wait(types=['killboss1'])
def wait_for_kill_boss_1():
    print('YOU KILLED BOSS 1!!!')
    return 'open up doorway'

@listener.wait(types=['one word:hi']) # example for 1 word (you JUST type 'hi' and nothing else)
def say hi():
    print('HI!!!!')
    return '00hi'

@listener.wait(types=['killboss2'])
def wait_for_kill_boss_2():
    print('CONGRATS! YOU KILLED BOSS 2!!!')
    print('well done, you finished the game!')
    return 'credits start'"""