import tkinter
from tkinter import ttk

window = tkinter.Tk()

def saludar(event):
    print("click en saludar")

def saludar2(event):
    print("Aguantaaaa")

def despida(event):
    window.quit()

boton = tkinter.Button(window, text='Rodorigo')
boton.pack()
boton.bind('<Button-1>', saludar)
boton.bind('<Double-1>', saludar2)

salir = tkinter.Button(window, text='Salir')
salir.pack()
salir.bind('<Button-1>', despida)

window.mainloop()