from tkinter import *

root = Tk()

radiovar = IntVar(value=-1)
for i in range(10):
    Radiobutton(root, text = i,
                      variable = radiovar,
                      value = i % 3).pack(side=LEFT, anchor=W)
mainloop()

