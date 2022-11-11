import tkinter
from tkinter import ttk
# posicion absoluta en base a coordenadas
window = tkinter.Tk()

label1 = tkinter.Label(window, text='Absolute position', bg='blue', fg='white')
label1.place(x=10, y=50)

label2 = tkinter.Label(window, text='OOOOOO MAI GAD', bg='red', fg='blue')
label2.place(relx=0.10, rely=0.15, relwidth=0.5, anchor='ne')

window.mainloop()