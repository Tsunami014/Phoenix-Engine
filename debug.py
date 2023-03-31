from copy import deepcopy
import side as s
import tkinter as tk
from tkinter import scrolledtext

g = s.Game()

print('loading classes...')

class Dropdown:
    def __init__(self, root, changedfunc, options=[], init=''):
        #The function to run when the dropdown gets updated
        self.changedfunc = changedfunc
        
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

class DebugInterface:
    def __init__(self):
        self.inps = []
        self.i = 0
        self.debugs = []
        self.dbugtyp = None
        self.end = {}
        self.ccroom = None
        self.setup()
    
    def setup(self):
        print('setting up tkinter...')
        self.root = tk.Tk()
        self.rootwidgets = []

        title_text = '"%s": by %s\n%s\nPress go to start' % (g.fc['card']['title'], g.fc['card']['author'], g.fc['card']['description'])

        self.game = tk.Label(self.root, text=title_text, relief='ridge', wraplength=400)
        self.game.pack(side='top', fill='x', pady=10, padx=10)

        self.subgame = tk.Label(self.root, text='', relief='ridge', wraplength=400)
        self.subgame.pack(side='top', fill='x', pady=10, padx=10)

        l1 = tk.Label(self.root, text='What do you do?')
        l1.pack()

        self.inp = tk.Entry(self.root, relief='sunken')
        self.inp.pack(side='top', fill='x', pady=10, padx=10)

        btn1 = tk.Button(self.root, text='go', command=self.go)
        btn1.pack(fill='x', pady=10, padx=10)

        l2 = tk.Label(self.root, text='Logs:')
        l2.pack(side='bottom')

        self.logs = tk.Label(self.root, text='Logs go here', relief='groove', wraplength=400)
        self.logs.pack(side='bottom', padx=10, pady=10, fill='x', before=l2)

        btn2 = tk.Button(self.root, text='show debug window', command=self.show_debug)
        btn2.pack(side='bottom', fill='x', pady=10, padx=10, before=self.logs)
        
        self.inp.bind('<Return>', self.go)
        self.inp.bind('<Up>', self.up)
        self.inp.bind('<Down>', self.dwn)
        s.clear()
        self.rootwidgets = {self.game, self.subgame, l1, self.inp, btn1, l2, self.logs, btn2}
        self.go()
        print('complete!')
        self.root.mainloop()
        
    def up(self, args=None):
        if self.i > 0:
            self.i -= 1
            self.inp.delete(0, len(self.inp.get()))
            self.inp.insert(0, self.inps[self.i])

    def dwn(self, args=None):
        if self.i < len(self.inps):
            self.i += 1
            self.inp.delete(0, len(self.inp.get()))
            try:
                self.inp.insert(0, self.inps[self.i])
            except IndexError:
                pass

    #args in these cases are just the keybinds when you press enter.
    def go(self, args=None, debug=True):
        croom = g.fc['rooms'][str(g.roomnum)]
        if self.inp.get() != '':
            self.inps.append(self.inp.get())
            self.i = len(self.inps)
            self.logs.config(text="\n".join([str(i) for i in g(self.inp.get(), g.roomnum, croom['objects'])]))
        self.game.config(text=croom['name'].capitalize()+'\n'+croom['description'])
        
        #How the second line works is it says you can not exit if there are no exits otherwise it states all the exits and the direction of exit.
        #How the 3 simmilar statements work: they basically make a string: "[item1, item2, item3]" for each item in the room's items that are of a certain type.
        txt = "It is%s dark.\n" % ("" if croom['dark'] else "n't") + \
            "You can " + ('not exit\n' if len(croom['exits']) == 0 else ('exit ' + ", ".join(["%s towards %s" % (s.pos[int(i)], \
                    g.fc["rooms"][str(croom['exits'][i])]["name"]) for i in croom['exits']]) + '\n') + \
            "There are these objects: " +         '['+"".join([i['identifier']+", " if i['type'] == 5 else '' for i in croom['objects']])+']\n' + \
            "You can see: " +                     '['+"".join([i['identifier']+", " if i['type'] == 6 else '' for i in croom['objects']])+']\n' + \
            "There are these people/monsters: " + '['+"".join([i['identifier']+", " if i['type'] == 4 else '' for i in croom['objects']])+']\n')
        self.subgame.config(text=txt)
        self.inp.delete(0, len(self.inp.get()))
        if debug: self.debug()

    def debug(self, *args):
        try:
            self.top
        except:
            return False
        croom = g.fc['rooms'][str(g.roomnum)]
        changed = False
        if self.ccroom != croom or self.end != croom:
            changed = True
            self.ccroom = deepcopy(croom)
            self.end = deepcopy(croom)
        self.l3.config(text='Debug \'%s\' (%s)' % (g.roomnum, croom['name']))
        
        try:
            prev = self.d.get()
            if not changed:
                self.save(True, self.d.prev, False)
        except:
            prev = list(croom.keys())[0]
            self.d = Dropdown(self.top, self.debug, list(croom.keys()), prev)
            self.d.pack()
        
        for i in self.debugs:
            if type(i) == tk.scrolledtext.ScrolledText:
                i.master.destroy()
                i.frame.destroy()
            i.destroy()
            del i
        
        self.debugs = []
        
        def sav(*args):
            self.save(True, prev)
            self.go(debug=False)

        if type(self.end[prev]) == bool:
            self.dbugtyp = bool
            self.debugs = [Dropdown(self.top, sav, ['True', 'False'], str(self.end[prev]))]
            self.debugs[0].pack()
        elif type(self.end[prev]) == int:
            self.dbugtyp = int
            self.debugs = [tk.Spinbox(self.top, from_=0, to=10)]
            self.debugs[0].pack()
            self.debugs[0].delete(0,"end")
            self.debugs[0].insert(0,2)
        #elif type(self.end[prev]) == list:
        #    frame = tk.Frame(self.top)
        #    self.debugs = [frame]
        #    for i in lit:
        #        self.debugs.append(Dropdown(lambda: None, frame, list(i.keys())))
        #        self.debugs[len(self.debugs)-1].pack()                    # not working yet...
        else:
            self.dbugtyp = str
            self.debugs = [scrolledtext.ScrolledText(self.top, wrap=tk.WORD,
                                        width=40, height=8,
                                        font=("Times New Roman", 15))]
            self.debugs[0].pack(fill='both', padx=10, pady=10)
        
            self.debugs[0].bind('<Return>', sav)
            self.debugs[0].delete('1.0', tk.END,)
            self.debugs[0].insert(tk.INSERT, str(self.end[prev]))

    def save(self, save=False, what_inend=None, update_game=True):
        if save:
            if self.dbugtyp == bool:
                self.end[what_inend] = self.debugs[0].get() == "True"
            elif self.dbugtyp == int:
                self.end[what_inend] = self.debugs[0].get()
            elif self.dbugtyp == str:
                self.end[what_inend] = self.debugs[0].get("1.0", tk.END).strip('\n \t')
            else:
                raise ValueError("Unknown type %s" % str(self.dbugtyp))
        
        if update_game:
            g.fc['rooms'][str(g.roomnum)] = self.end

    def upload(self):
        print('upload to file')

    def reset(self):
        g.fc['rooms'][str(g.roomnum)] = g.tosavefc['rooms'][str(g.roomnum)]
        self.debug()

    def show_debug(self):
        self.top = tk.Toplevel(self.root)
        self.l3 = tk.Label(self.top, text='Debug', relief='solid')
        self.l3.pack(side='top', fill='x', pady=10, padx=10)
        
        btn3 = tk.Button(self.top, text='sync changes', command=self.save)
        btn3.pack(side='bottom', fill='x', pady=10, padx=10)
        
        btn4 = tk.Button(self.top, text='save', command=self.upload)
        btn4.pack(side='bottom', fill='x', pady=10, padx=10, before=btn3)
        
        btn5 = tk.Button(self.top, text='reset level to file original', command=self.reset)
        btn5.pack(side='bottom', fill='x', pady=10, padx=10, before=btn4)
        
        self.debug()

        self.topwidgets = [self.l3, btn3, btn4, btn5]
        self.top.mainloop()
    
d = DebugInterface()