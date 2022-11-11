import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)

nombres = ['Rodrigo', 'Benjamin', 'Dante', 'Melanie', 'Ramona']
nombres_items = tkinter.StringVar(value=nombres)
listbox = tkinter.Listbox(window, height=10, listvariable=nombres_items)
listbox.grid(column=0, row=0, sticky=tkinter.W)

label = ttk.Label(window, text="Nombres")
label.grid(column=0, row=1, padx=5, pady=5)


window.mainloop()