from tkinter import *
from grid2 import gridbox, packbox

root = Tk()
Button(root, text='Quit', command=root.quit).pack(side=BOTTOM, pady=20)
Label(root, text='GRID').pack(expand=True, padx=20, pady=20)
gridFrm = Frame(root, relief=GROOVE)
gridFrm.pack(expand=True, fill=BOTH)
gridbox(gridFrm)

Label(root, text='PACK').pack(expand=True, padx=20, pady=20)
packFrm = Frame(root, relief=SUNKEN)
packFrm.pack(expand=True, fill=BOTH)
packbox(packFrm)
mainloop()

