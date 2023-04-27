try:
    import connector as c
except ModuleNotFoundError:
    import other.connector as c
from difflib import get_close_matches as GCM

listener = c.EventListener()

monsters = ['bokoblin']

fight = 0

@listener.wait(types=['init'])
def init(self):
    self.fight = False

@listener.wait(types=['move']) # check each move to see if it sparks a fight
def wait_for_move(self):
    tot = []
    for i in self.fc['rooms'][str(self.roomnum)]['objects']:
        l = GCM(i['name'], monsters, n=1, cutoff=self.cutoff)
        if l:
            tot.append(l[0])
    if tot:
        global fight
        fight = 1
        return '00OH NO! THERE IS A ' + " AND A ".join(tot) + "! THEY START A FIGHT!!! (you can no longer exit);6~!!4~"#code to print and no longer exit
    return ''

@listener.wait(types=['action'])
def action(self):
    # self.prev_action, counterproductively, is the current action and you can use said variable here!
    if self.fight:
        monster_turn(self)
    if fight == 1:
        global fight
        fight = 0
        self.fight = True

def monster_turn(self):
    pass

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