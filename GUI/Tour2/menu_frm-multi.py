import sys, os
import tkinter as tk
from tkinter.constants import *
from menu_frm import MakeMenuFrame

root = tk.Tk()
for i in range(3):
    frm = tk.Frame(root)
    frm.pack(expand=True, fill=BOTH)
    MakeMenuFrame(frm)
    frm.config(bd=4, relief=SUNKEN)
    tk.Label(frm, bg='black', fg='white', text='MultiFrame Menu',
             font=('times', 20, 'bold italic'), height=5, width=35).pack()
tk.Button(root, text='Quit', command=root.quit).pack(expand=True)
root.title(os.path.basename(sys.argv[0]))
root.mainloop()

