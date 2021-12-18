from tkinter import *

def onMove(scl):
    print(scl.get())

root = Tk()

(scl := Scale(root, from_=-100,
        to=100, length=300,
        resolution=25, showvalue=YES,
        tickinterval=50, command=lambda val: print(val),
)).pack(expand=True, fill=BOTH)

Button(root, text='State',
       command=lambda: onMove(scl)
).pack(expand=True, fill=BOTH)

root.mainloop()

