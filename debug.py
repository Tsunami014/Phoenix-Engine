from copy import deepcopy
import side as s
import tkinter as tk
from tkinter import scrolledtext

g = s.Game()

print('setting up tkinter...')

inps = []
i = 0
debugs = []
dbugtyp = None
end = {}
ccroom = None

class Dropdown:
    def __init__(self, root, options=[], init='', changedfunc=None):
        
        #The function to run when the dropdown gets updated
        self.changedfunc = changedfunc if changedfunc != None else debug
        
        # datatype of menu text
        self.clicked = tk.StringVar()
        
        # initial menu text
        if init != '': self.clicked.set(init)
        else: self.clicked.set(options[0])
        self.clicked.trace("w", self.changed)
        
        self.now = self.get()
        self.prev = ''
        
        # Create Dropdown menu
        self.drop = tk.OptionMenu(root, self.clicked, *options )
    
    def pack(self, *args):
        self.drop.pack(args)
    
    def get(self):
        return self.clicked.get()
    
    def destroy(self):
        self.drop.destroy()
        del self

    def changed(self, *args):
        self.prev = self.now
        self.now = self.get()
        self.changedfunc()

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
    debug()

def debug(*args):
    global l3, debugs, top, d, debuginp, ccroom, end, dbugtyp
    try:
        top
    except:
        return False
    croom = g.fc['rooms'][str(g.roomnum)]
    changed = False
    if ccroom != croom or end != croom:
        changed = True
        ccroom = deepcopy(croom)
        end = deepcopy(croom)
    l3.config(text='Debug \'%s\' (%s)' % (g.roomnum, croom['name']))
    
    try:
        prev = d.get()
        if not changed:
            save(False)
    except:
        prev = list(croom.keys())[0]
        d = Dropdown(top, list(croom.keys()), prev)
        d.pack()
    
    for i in debugs:
        if type(i) == tk.scrolledtext.ScrolledText:
            i.master.destroy()
            i.frame.destroy()
        i.destroy()
        del i
    
    debugs = []
    
    sav = lambda *args: save(False)

    if type(end[prev]) == bool:
        dbugtyp = bool
        debugs = [Dropdown(top, ['True', 'False'], str(end[prev]), sav)]
        debugs[0].pack()
    elif type(end[prev]) == int:
        dbugtyp = int
        debugs = [tk.Spinbox(top, from_=0, to=10)]
        debugs[0].pack()
        debugs[0].delete(0,"end")
        debugs[0].insert(0,2)
    #elif type(end[prev]) == list:
    #    frame = tk.Frame(top)
    #    debugs = [frame]
    #    for i in lit:
    #        debugs.append(Dropdown(frame, list(i.keys())))
    #        debugs[len(debugs)-1].pack()                    # not working yet...
    else:
        dbugtyp = str
        debugs = [scrolledtext.ScrolledText(top, wrap=tk.WORD,
                                      width=40, height=8,
                                      font=("Times New Roman", 15))]
        debugs[0].pack(fill='both', padx=10, pady=10)
    
        debugs[0].bind('<Return>', sav)
        debugs[0].delete('1.0', tk.END,)
        debugs[0].insert(tk.INSERT, str(end[prev]))

def save(update_game=True):
    global dbugtyp, end, d, debugs, g
    if dbugtyp == bool:
        end[d.prev] = debugs[0].get() == "True"
    elif dbugtyp == int:
        end[d.prev] = debugs[0].get()
    elif dbugtyp == str:
        end[d.prev] = debugs[0].get("1.0", tk.END)
    else:
        raise ValueError("Unknown type %s" % str(dbugtyp))
    
    if update_game:
        g.fc['rooms'][str(g.roomnum)] = end

def upload():
    print('upload to file')

def reset():
    global g
    g.fc['rooms'][str(g.roomnum)] = g.tosavefc['rooms'][str(g.roomnum)]
    debug()

def show_debug():
    global top, l3, btn3, debuginp, btn4, btn5
    top = tk.Toplevel(root)
    l3 = tk.Label(top, text='Debug', relief='solid')
    l3.pack(side='top', fill='x', pady=10, padx=10)
    
    btn3 = tk.Button(top, text='sync changes', command=save)
    btn3.pack(side='bottom', fill='x', pady=10, padx=10)
    
    btn4 = tk.Button(top, text='save', command=upload)
    btn4.pack(side='bottom', fill='x', pady=10, padx=10, before=btn3)
    
    btn5 = tk.Button(top, text='reset level to file original', command=reset)
    btn5.pack(side='bottom', fill='x', pady=10, padx=10, before=btn4)
    
    debug()

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