try:
    import connector as c
except ModuleNotFoundError:
    import other.connector as c
from difflib import get_close_matches as GCM

from json import load
from random import randint, choice

#If at any time you want to stop the current action from being applied, then in the externals just pop in a "の" anywhere. It will get removed before being executed.

listener = c.EventListener()

#monsters dict in format: {name: [power (see below list powers for the number), hp]}
monsters = {'bokoblin': [0, 50]}
powers = [(10, {6:['tried to hit you... But it missed!', '... tried to hit you but you blocked!', 'hit your shield!'], 11: 'hit you for {5} HP!;71hp = 1{5}'})]

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
                return '00The %s ' % self.name + end.format(*[str(randint(1, i+1)) for i in range(1, 10)]) # so you can go 'it hit you for {5} HP!' and that {5} will be replaced with a random number from 1 to 5
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
    tot = []
    for i in self.fc['rooms'][str(self.roomnum)]['objects']:
        l = GCM(i['name'], monsters.keys(), n=1, cutoff=self.cutoff)
        if l:
            tot.append(l[0])
            self.fc['rooms'][str(self.roomnum)]['objects'].remove(i)
    if tot:
        self.fight = True
        self.curmonsters = [Monster(j) for j in tot]
        return '00OH NO! THERE IS A ' + " AND A ".join(tot) + r"! THEY START A FIGHT!!! (you can no longer exit);5~!!4~!!{}"#code to print and no longer exit
    return ''

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
                deps = battle[self.prev_action]['else']
        if deps == None: skip = ''
        else: skip = 'の'
        if type(deps) == list:
            value = randint(0, deps[0])
            for i in deps[1:].keys(): # for each number in the list of numbers:
                if i >= value: # if the value is closer to i than the last one (in the case of the first one, it must be less than 2 distance away)
                    end = deps[1:][i] if type(deps[1:][i]) == str else choice(deps[1:][i])
                    end = end.format(*[str(randint(1, i+1)) for i in range(1, 10)]) # so you can go 'it hit you for {5} HP!' and that {5} will be replaced with a random number from 1 to 5
                    return ('%s%s%s%s' % (skip, mt, (';' if mt else ''), end))
            return '00CODING ERROR: %s' % str(self)
        elif deps == None:
            return ('%s%s' % (skip, mt))
        else:
            return ('%s%s%s%s' % (skip, mt, (';' if mt else ''), deps.format(*[str(randint(1, i+1)) for i in range(1, 10)]))) # so you can go 'it hit you for {5} HP!' and that {5} will be replaced with a random number from 1 to 5
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

@listener.wait(types=['one word:hi']) # example for 1 word
def say hi():
    print('HI!!!!')
    return '00hi'

@listener.wait(types=['killboss2'])
def wait_for_kill_boss_2():
    print('CONGRATS! YOU KILLED BOSS 2!!!')
    print('well done, you finished the game!')
    return 'credits start'"""