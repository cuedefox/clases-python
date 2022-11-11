import tkinter
import random
from tkinter import ttk

window = tkinter.Tk()

colors = ['red', 'blue', 'yellow', 'black', 'white', 'purple', 'orange']

for x in range(0, 10):
    color1 = random.randint(0, len(colors)-1)
    color2 = random.randint(0, len(colors)-1)
    label = tkinter.Label(window, text='Rodorigo Verugara', bg=colors[color1], fg=colors[color2])
    label.place(x = random.randint(0, 100), y = random.randint(0, 100))

window.mainloop()