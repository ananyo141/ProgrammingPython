from tkinter import *

root = Tk()

for i in range(5):
    for j in range(4):
        Label(root, text='{row}.{col}'.format(row=i, col=j),
                relief=GROOVE,
        ).grid(row=i, column=j, sticky=NSEW)
        root.columnconfigure(j, weight=1)
    root.rowconfigure(i, weight=1)

mainloop()

