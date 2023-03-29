import side as s
import tkinter as tk

g = s.Game()

print('setting up tkinter...')

inps = []
i = 0

def up(args=None):
    global i, inps
    if i > 0:
        i -= 1
        inp.delete(0, len(inp.get()))
        inp.insert(0, inps[i])

def dwn(args=None):
    global i, inps
    if i < len(inps):
        i += 1
        inp.delete(0, len(inp.get()))
        try:
            inp.insert(0, inps[i])
        except IndexError:
            pass

#args in these cases are just the keybinds when you press enter.
def go(args=None):
    global i, inps
    croom = g.fc['rooms'][str(g.roomnum)]
    if inp.get() != '':
        inps.append(inp.get())
        i = len(inps)
        logs.config(text="\n".join([str(i) for i in g(inp.get(), g.roomnum, croom['objects'])]))
    game.config(text=croom['name'].capitalize()+'\n'+croom['description'])
    
    #How the second line works is it says you can not exit if there are no exits otherwise it states all the exits and the direction of exit.
    #How the 3 simmilar statements work: they basically make a string: "[item1, item2, item3]" for each item in the room's items that are of a certain type.
    txt = "It is%s dark.\n" % ("" if croom['dark'] else "n't") + \
        "You can " + ('not exit\n' if len(croom['exits']) == 0 else ('exit ' + ", ".join(["%s towards %s" % (s.pos[int(i)], \
                g.fc["rooms"][str(croom['exits'][i])]["name"]) for i in croom['exits']]) + '\n') + \
        "There are these objects: " +         '['+"".join([i['identifier']+", " if i['type'] == 5 else '' for i in croom['objects']])+']\n' + \
        "You can see: " +                     '['+"".join([i['identifier']+", " if i['type'] == 6 else '' for i in croom['objects']])+']\n' + \
        "There are these people/monsters: " + '['+"".join([i['identifier']+", " if i['type'] == 4 else '' for i in croom['objects']])+']\n')
    subgame.config(text=txt)
    inp.delete(0, len(inp.get()))
    pass

def debug(args=None):
    print('debug', args)

def search():
    print('search')

def save():
    print('save')

def show_debug():
    global top, l3, btn3, debuginp, btn4, btn5
    top = tk.Toplevel(root)
    l3 = tk.Label(top, text='Debug window', relief='solid')
    l3.pack(side='top', fill='x', pady=10, padx=10)
    
    btn3 = tk.Button(top, text='search for things to debug', command=search)
    btn3.pack(side='top', fill='x', pady=10, padx=10)
    
    debuginp = tk.Entry(top)
    debuginp.pack(fill='both', padx=10, pady=10)
    
    debuginp.bind('<Return>', debug)
    
    btn4 = tk.Button(top, text='debug', command=debug)
    btn4.pack(fill='x', pady=10, padx=10)
    
    btn5 = tk.Button(top, text='save', command=save)
    btn5.pack(side='bottom', fill='x', pady=10, padx=10)

    top.mainloop()

root = tk.Tk()

title_text = '"%s": by %s\n%s\nPress go to start' % (g.fc['card']['title'], g.fc['card']['author'], g.fc['card']['description'])

game = tk.Label(root, text=title_text, relief='ridge', wraplength=400)
game.pack(side='top', fill='x', pady=10, padx=10)

subgame = tk.Label(root, text='', relief='ridge', wraplength=400)
subgame.pack(side='top', fill='x', pady=10, padx=10)

l1 = tk.Label(root, text='What do you do?')
l1.pack()

inp = tk.Entry(root, relief='sunken')
inp.pack(side='top', fill='x', pady=10, padx=10)

btn1 = tk.Button(root, text='go', command=go)
btn1.pack(fill='x', pady=10, padx=10)

btn2 = tk.Button(root, text='show debug window', command=show_debug)
btn2.pack(side='bottom', fill='x', pady=10, padx=10)

logs = tk.Label(root, text='Logs go here', relief='groove', wraplength=400)
logs.pack(side='bottom', padx=10, pady=10, fill='x')

l2 = tk.Label(root, text='Logs:')
l2.pack(side='bottom')

inp.bind('<Return>', go)
inp.bind('<Up>', up)
inp.bind('<Down>', dwn)
s.clear()
go()
print('complete!')
root.mainloop()