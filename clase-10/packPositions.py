import tkinter

window = tkinter.Tk()

label1= tkinter.Label(window, text='Label 1', bg='blue', fg='white')
label1.pack(ipadx=45, ipady=45, fill='x')
label2 = tkinter.Label(window, text='Label 2', bg='red', fg='white')
label2.pack(ipadx=45, ipady=45, fill='x')
label3 = tkinter.Label(window, text='Label 3', bg='green', fg='white')
label3.pack(ipadx=45, ipady=45, fill='x')
label4 = tkinter.Label(window, text='Label 4', bg='yellow', fg='white')
label4.pack(ipadx=45, ipady=45, side='left')
label5 = tkinter.Label(window, text='Label 5', bg='purple', fg='white')
label5.pack(ipadx=45, ipady=45, side='left')
label6 = tkinter.Label(window, text='Label 6', bg='orange', fg='white')
label6.pack(ipadx=45, ipady=45, side='left')



window.mainloop()