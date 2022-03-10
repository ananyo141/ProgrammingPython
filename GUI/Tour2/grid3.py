from tkinter import *
from grid1 import colors

def expandPack(parent):
    packFrm = Frame(parent)
    packFrm.pack(expand=True, fill=BOTH)
    Label(packFrm, text='Pack').pack(expand=True, fill=X)
    for color in colors:
        rowFrm = Frame(packFrm)
        rowFrm.pack(expand=True, fill=BOTH)
        Label(rowFrm, text=color, 
              width=25, relief=RIDGE
        ).pack(side=LEFT, expand=True, fill=BOTH)
        Entry(rowFrm, bg=color, width=40, relief=GROOVE).pack(expand=True,
                fill=BOTH, side=LEFT)

def expandGrid(parent):
    gridFrm = Frame(parent)
    gridFrm.grid(row=0, column=0, sticky=NSEW)
    # make grid container expandable
    parent.rowconfigure(0, weight=1)
    parent.columnconfigure(0, weight=1)
    
    Label(gridFrm, text='Grid').grid(row=0, column=0, columnspan=2)
    gridFrm.rowconfigure(0, weight=1)
    gridFrm.columnconfigure(0, weight=1)
    for ind, color in enumerate(colors):
        Label(gridFrm, text=color, relief=RIDGE, width=25).grid(row=ind+1,
                column=0, sticky=NSEW)
        Entry(gridFrm, bg=color, relief=GROOVE, width=40).grid(row=ind+1,
                column=1, sticky=NSEW)
        gridFrm.rowconfigure(ind, weight=1) # make rows expandable
    gridFrm.columnconfigure(0, weight=1)    # make both columns
    gridFrm.columnconfigure(1, weight=1)    # on frame expandable

def main():
    root = Tk()
    expandPack(root)
    expandGrid(Toplevel(root))
    mainloop()

if __name__ == '__main__':
    main()

