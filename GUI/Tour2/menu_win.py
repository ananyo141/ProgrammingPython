import tkinter as tk
from tkinter import messagebox
from tkinter.constants import *

class MakeMenu:
    def __init__(self, parent):
        self.parent  = parent                 # save parent toplevel widget
        self.topmenu = tk.Menu(self.parent)   # create a top menu bar
        self.parent.config(menu=self.topmenu) # link parent menu to menu bar
        self.filemenu()
        self.editmenu()

    def filemenu(self):
        file = tk.Menu(self.topmenu)
        self.topmenu.add_cascade(label='File', menu=file, underline=0)

        file.add_command(label='New',  command=lambda: self.notimplemented('New'),  underline=0)
        file.add_command(label='Open', command=lambda: self.notimplemented('Open'), underline=0)
        file.add_command(label='Quit', command=self.quit, underline=0)

    def editmenu(self):
        edit = tk.Menu(self.topmenu, tearoff=False)
        self.topmenu.add_cascade(label='Edit', menu=edit, underline=0)

        edit.add_command(label='Cut',   command=self.notimplemented, underline=0)
        edit.add_command(label='Paste', command=self.notimplemented, underline=0)
        edit.add_separator()

        submenu = tk.Menu(edit)
        edit.add_cascade   (label='Stuff', menu=submenu, underline=0)
        submenu.add_command(label='Spam', command=self.notimplemented, underline=0)
        submenu.add_command(label='Eggs', command=self.notimplemented, underline=0)
    
    def quit(self):
        self.parent.quit()

    def notimplemented(self, feat=None):
        feat = feat if feat else 'This feature'
        tk.messagebox.showerror('Not Implemented', feat + ' is not yet available...')

if __name__ == '__main__':
    root = tk.Tk()
    root.title('MenuBar')
    MakeMenu(root)  # used the class as an expandable function
    tk.Label(root, text='Window Menu Basics', 
                   bd=3, width=40, height=8,
                   relief=GROOVE, bg='beige'
    ).pack(expand=True, fill=BOTH)
    root.mainloop()

