#import side
import tkinter as tk

#g = side.Game()

root = tk.Tk()

#title_text = '"%s": by %s\n%s\nPress enter to start' % (g.fc['card']['title'], g.fc['card']['author'], g.fc['card']['description'])
title_text = "Hello! This is where the game text would go,\nbut it isn't here because it makes testing the interface harder."

game = tk.Label(root, text=title_text, relief='ridge')
#game.grid(row=1, column=1, padx=10, pady=10)
game.pack(side='top', fill='x', pady=10, padx=10)

l1 = tk.Label(root, text='Input:')
#l1.grid(row=2, column=0)
l1.pack()

inp = tk.Entry(root, relief='sunken')
#inp.grid(row=2, column=1, padx=10, pady=10)
inp.pack(side='top', fill='x', pady=10, padx=10)

btn1 = tk.Button(root, text='go')
#btn1.grid(row=2, column=2)
btn1.pack(fill='x', pady=10, padx=10)

btn2 = tk.Button(root, text='show debug window', command=show_debug)
#btn2.grid(row=2, column=2)
btn2.pack(side='bottom', fill='x', pady=10, padx=10)

logs = tk.Label(root, text='Logs go here', relief='groove')
#logs.grid(row=3, column=2, padx=10, pady=10)
logs.pack(side='bottom', padx=10, pady=10, fill='x')

l2 = tk.Label(root, text='Logs:')
#l2.grid(row=3, column=0)
l2.pack(side='bottom')

root.mainloop()