import connector as c
listener = c.EventListener()
    
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