from tkinter import *
from grid1 import colors

LAB_W = 25
ENT_W = 40

def gridbox(parent):
    for ind, color in enumerate(colors):
        Label(parent, text=color, width=LAB_W,
              relief=GROOVE).grid(row=ind, column=0)
        ent = Entry(parent, bg=color, width=ENT_W, fg='black', relief=SUNKEN)
        ent.grid(row=ind, column=1)
        ent.insert(END, 'grid')

def packbox(parent):
    for color in colors:
        frm = Frame(parent)
        frm.pack()
        Label(frm, text=color, width=LAB_W, relief=GROOVE).pack(side=LEFT)
        ent = Entry(frm, bg=color, fg='black', width=ENT_W, relief=SUNKEN)
        ent.insert(END, 'pack')
        ent.pack(side=RIGHT)

def main():
    root = Tk()
    packbox(Toplevel())
    gridbox(Toplevel())
    Button(root, text='Quit', command=root.quit).pack()
    mainloop()

if __name__ == '__main__':
    main()

