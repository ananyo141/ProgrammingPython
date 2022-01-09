import tkinter as tk
from tkinter import messagebox
from tkinter.constants import *

class MakeMenuFrame:
    def __init__(self, parent=None):
        self.menubar = tk.Frame(parent)
        self.menubar.pack(side=TOP, fill=X)
        self.filemenu()
        self.editmenu()

    def filemenu(self):
        menu = tk.Menubutton(self.menubar, text='File', underline=0)
        menu.pack(side=LEFT)
        file = tk.Menu(menu, tearoff=False)
        menu.config(menu=file)

        file.add_command(label='New',  command=self.notdone, underline=0)
        file.add_command(label='Open', command=self.notdone, underline=0)
        file.add_command(label='Quit', command=self.menubar.master.quit, underline=0)

    def editmenu(self):
        menu = tk.Menubutton(self.menubar, text='Edit', underline=0)
        menu.pack(side=LEFT)
        edit = tk.Menu(menu, tearoff=False)
        menu.config(menu=edit)

        edit.add_command(label='Cut',   command=self.notdone, underline=0)
        edit.add_command(label='Paste', command=self.notdone, underline=0)

        submenu = tk.Menu(edit, tearoff=False)
        edit.add_cascade(label='Stuff', menu=submenu, underline=0)
        submenu.add_command(label='Spam', command=self.notdone, underline=0)
        submenu.add_command(label='Eggs', command=self.notdone, underline=0)

    def notdone(self):
        tk.messagebox.showerror('Not Implemented', 'This feature is not implemented')

if __name__ == '__main__':
    root = tk.Tk()
    MakeMenuFrame(root)
    tk.Label(root, text='Frame Menu', bd=3, relief=RAISED, 
             bg='maroon', fg='white', width=20, height=5).pack(expand=True, fill=BOTH)
    root.mainloop()

