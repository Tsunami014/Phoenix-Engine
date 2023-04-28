try:
    import connector as c
except ModuleNotFoundError:
    import other.connector as c
from difflib import get_close_matches as GCM

from random import randint, choice

listener = c.EventListener()

monsters = {'bokoblin': 0}
curmonsters = []
powers = [(10, {6:['tried to hit you... But it missed!', '... tried to hit you but you blocked!', 'hit you...r shield!'], 11: 'hit you for {5} HP!;71hp = 1{5}'})]

fight = 0

class Monster:
    def __init__(self, name: str, power: int=-1):
        self.name = name
        self.power = powers[power if power != -1 else monsters[name]]
        self.roll = self.power[0]
        self.power = self.power[1]
    
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

    def your_turn(self, player):
        print(player.prev_action)
        return ''

@listener.wait(types=['init'])
def init(self):
    self.fight = False
    self.hp = 100
    self.inv = {}
    return ''

@listener.wait(types=['move']) # check each move to see if it sparks a fight
def wait_for_move(self):
    tot = []
    for i in self.fc['rooms'][str(self.roomnum)]['objects']:
        l = GCM(i['name'], monsters.keys(), n=1, cutoff=self.cutoff)
        if l:
            tot.append(l[0])
    if tot:
        global fight, curmonsters
        fight = 1
        curmonsters.extend([Monster(j) for j in tot])
        return '00OH NO! THERE IS A ' + " AND A ".join(tot) + "! THEY START A FIGHT!!! (you can no longer exit);6~!!4~"#code to print and no longer exit
    return ''

@listener.wait(types=['action'])
def action(self):
    # self.prev_action, counterproductively, is the current action and you can use said variable here!
    if self.fight:
        return monster_turn(self)
    else:
        global fight
        if fight == 1:
            fight = 0
            self.fight = True
    return ''

def monster_turn(player_self):
    global curmonsters
    end = ';'
    for i in curmonsters:
        end += i.your_turn(player_self) + ';'
        end += i.its_turn() + ';'
    return end[1:-1]

#by the way the rest of these are for show and do not actually do stuff yet
#please note these (below) are examples of events, and are not actual events.
"""
@listener.wait(types=['killboss1'])
def wait_for_kill_boss_1():
    print('YOU KILLED BOSS 1!!!')
    return 'open up doorway'

@listener.wait(types=['killboss2'])
def wait_for_kill_boss_2():
    print('CONGRATS! YOU KILLED BOSS 2!!!')
    print('well done, you finished the game!')
    return 'credits start'"""