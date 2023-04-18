import friends_code
import connector as c
listener = c.EventListener()

while True:
    print('*****', listener.event(input('> ')))