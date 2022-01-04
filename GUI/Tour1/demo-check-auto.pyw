from tkinter import *

root = Tk()
variables = []
for i in range(10):
    var = IntVar()
    Checkbutton(root, text=str(i+1), variable=var).pack(side=LEFT)
    variables.append(var)

mainloop()
print(*map(lambda x: x.get(), variables))
    
