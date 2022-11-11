import tkinter

window = tkinter.Tk()

label_saludo = tkinter.Label(window, text='Hola', bg='black', fg='white')
label_saludo.pack(ipadx=50, ipady=50, fill='both')
# ipad es para el padding, fill es para estirar en un eje
label_despedida = tkinter.Label(window, text='Adios', bg='red', fg='green')
label_despedida.pack(ipadx=50, ipady=50, fill='both')
# La geometria pack se utiliza para ubicar elementos de arriba a abajo o de izquierda a derecha
window.mainloop()