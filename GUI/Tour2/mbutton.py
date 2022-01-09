import tkinter as tk
from tkinter.constants import *

root = tk.Tk()
mbutton = tk.Menubutton(root, text='Food', underline=0)

foodmenu = tk.Menu(mbutton)
mbutton.config(menu=foodmenu)
foodopts = ('spam', 'eggs', 'bacon')
for foodopt in foodopts:
    foodmenu.add_command(label=foodopt, command=root.quit, underline=0)

mbutton.config(bg='white', fg='grey', bd=3, relief=GROOVE)
mbutton.pack(fill=X)
root.mainloop()

