import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=2)
window.columnconfigure(1, weight=0)

def resetear(event):
    selected.set(0)

selected = tkinter.StringVar()
radio_button1 = ttk.Radiobutton(window, text='si', value=1, variable=selected)
radio_button2 = ttk.Radiobutton(window, text='no', value=2, variable=selected)
radio_button3 = ttk.Radiobutton(window, text='quiza', value=3, variable=selected)
reset_button = ttk.Button(window, text='Resetear')
radio_button1.grid(column=0, row=0, padx=5, pady=5)
radio_button2.grid(column=0, row=1, padx=5, pady=5)
radio_button3.grid(column=0, row=2, padx=5, pady=5)
reset_button.grid(column=1, row=0, padx=5, pady=5)
reset_button.bind('<Button-1>', resetear)

window.mainloop()