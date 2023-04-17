#This file is meant to be for using in all of your external files. Make a file (like locks.py) and use this structure by importing the file.
#Full documentation on how to use later in the file.

"""events:
type: int - event code, unique to whether you are pushing something or going somewhere
"""

class EventListener(object):
    all_funcs = {}
    def wait(self, types):
        def main(func):
            for typ in types:
                try:
                    self.all_funcs[typ].append(func)
                except:
                    self.all_funcs[typ] = [func]
            return func
        return main
    def event(self, type):
        endcode = ';'
        if type in self.all_funcs.keys():
            for i in self.all_funcs[type]:
                endcode += i() + ';'
        return endcode[1:-1]

if __name__ == '__main__':
    listener = EventListener()
    
    #please note these are examples of events, and are not actual events.
    @listener.wait(types=['enter1north', 'enter1south']) # Wait for certain events to happen
    def wait_for_going_in_room_1():
        print('entered room 1!!!!!!!!')
        return 'now do some stuff modifying the room here!!!!!!!!'
    
    @listener.wait(types=['killboss1'])
    def wait_for_kill_boss_1():
        print('YOU KILLED BOSS 1!!!')
        return 'open up doorway'
    
    @listener.wait(types=['killboss2'])
    def wait_for_kill_boss_2():
        print('CONGRATS! YOU KILLED BOSS 2!!!')
        print('well done, you finished the game!')
        return 'credits start'

    while True:
        print('*****', listener.event(input('> ')))