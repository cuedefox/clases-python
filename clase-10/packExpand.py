import tkinter

window = tkinter.Tk()

label_saludo = tkinter.Label(window, text='Hola', bg='black', fg='white')
label_saludo.pack(ipadx=50, ipady=50, expand=True, side='left')
# expand centra el elemento, side es para posicionar en una zona
label_despedida = tkinter.Label(window, text='Adios', bg='red', fg='green')
label_despedida.pack(fill='both', expand=True, side='right')

window.mainloop()