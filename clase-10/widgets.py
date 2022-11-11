import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
window.columnconfigure(2, weight=3)
# frame es una seccion
frame = ttk.Frame(window, relief='sunken')
frame.grid(column=0, row=0, sticky=tkinter.W)
label = ttk.Label(frame, text='Hola')
label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)
# listbox
nombres = ['Rodrigo', 'Benjamin', 'Dante', 'Melanie', 'Ramona']
nombres_items = tkinter.StringVar(value=nombres)
listbox = tkinter.Listbox(window, height=10, listvariable=nombres_items)
listbox.grid(column=1, row=0, sticky=tkinter.W)
# radiobutton
selected = tkinter.StringVar()
radio_button1 = ttk.Radiobutton(window, text='si', value=1, variable=selected)
radio_button2 = ttk.Radiobutton(window, text='no', value=2, variable=selected)
radio_button3 = ttk.Radiobutton(window, text='quiza', value=3, variable=selected)
radio_button1.grid(column=2, row=0, padx=5, pady=5)
radio_button2.grid(column=2, row=1, padx=5, pady=5)
radio_button3.grid(column=2, row=2, padx=5, pady=5)
# check
# command = asigna una variable al boton
selected2 = tkinter.StringVar()
checkbox = ttk.Checkbutton(window, text='Acepto condiciones', variable=selected2)
checkbox.grid(column=1, row=1)

window.mainloop()