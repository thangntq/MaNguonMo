import numpy as np
from tkinter import *
from tkinter.ttk import *


win = Tk()
win.title("TAO MANG")
win.geometry('800x800')
cot1 = Label(win, text="Cot 1")
cot1.grid(column=1, row=0)
cot2 = Label(win, text="Cot 2")
cot2.grid(column=2, row=0)
cot3 = Label(win, text="Cot 3")
cot3.grid(column=3, row=0)
hang1 = Label(win, text="Hang 1")
hang1.grid(column=0, row=1)
hang2 = Label(win, text="Hang 2")
hang2.grid(column=0, row=2)

a1 = Entry(win, width=15)
a1.grid(column=1, row=1)
a2 = Entry(win, width=15)
a2.grid(column=2, row=1)
a3 = Entry(win, width=15)
a3.grid(column=3, row=1)
b1 = Entry(win, width=15)
b1.grid(column=1, row=2)
b2 = Entry(win, width=15)
b2.grid(column=2, row=2)
b3 = Entry(win, width=15)
b3.grid(column=3, row=2)


def thuchien():
    na1 = float(a1.get())
    na2 = float(a2.get())
    na3 = float(a3.get())
    nb1 = float(b1.get())
    nb2 = float(b2.get())
    nb3 = float(b3.get())

    X = np.array([[na1, na2, na3], [nb1, nb2, nb3]], np.float32)
    X = Label(win,text=" " +str(X))
    X.place(x=20, y=120)


but = Button(win, text="KET QUA", command=thuchien)
but.grid(column=0, row=5)
win.mainloop()
