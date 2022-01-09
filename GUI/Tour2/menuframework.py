import tkinter as tk
from tkinter import messagebox
from tkinter.constants import *

# A wrapper class that automates the creation of menu options given the labels
# and their corresponding command handlers.
class MakeMenuWin:
    def __init__(self, parent=None):
        ''' Construct an object and attach a menu to it '''
        self.parent  = tk.Toplevel() if parent is None else parent
        self.topmenu = tk.Menu(parent)
        self.parent.config(menu=self.topmenu)

    def create_menu(self, menu=None, label='New', options=(), tearoff=False):
        ''' Take a label and tuple of (option, command handler) to construct
        the corresponding dropdown menu and return the linked menu widget '''
        if menu is None: menu = self.topmenu
        dropmenu = tk.Menu(menu, tearoff=tearoff)
        menu.add_cascade(label=label, menu=dropmenu, underline=0)
        self.add_options(dropmenu, options)
        return dropmenu

    def add_options(self, menu, options):
        ''' Add options to an existing and previously returned menu widget '''
        for option, handler in options:
            menu.add_command(label=option, command=handler, underline=0)

def testFrameWork():
    root = tk.Tk()
    warningHandler = lambda: tk.messagebox.showerror('Not Implemented', 'This feature '
                                                     'is not implemented')
    donothingHandler = lambda: None
    handler = donothingHandler

    tk.Label(root, text='Menu Framework demonstration',
                   width=30, height=8, fg='magenta', bg='blue',
                   relief=GROOVE, bd=3, font=('times', 14, 'italic'),
    ).pack(expand=True, fill=BOTH)
    # Create menu
    menu = MakeMenuWin(root)
    # Create menu and entries
    file = menu.create_menu(label='File', options=(('New',  handler),
                                                   ('Open', handler),
                                                   ('Print',handler)))
    editOptions = ('View', 'Save', 'Save As')
    edit = menu.create_menu(label='Edit', options=((op, handler) for op in editOptions))
    menu.create_menu(menu=edit, label='Expand', options=(('Tinker', handler),
                                                         ('Tupper', handler)))
    # Create submenu from previously created menu
    menu.create_menu(menu=file, label='Sub', options=(('this', handler),
                                                ('ok',   handler)))
    # Add a menu entry after previously adding
    menu.add_options(file, (('Quit', root.quit),))

    # Add a new menu
    menu.create_menu(label='View', options=(('Present', handler),
                                      ('Show',    handler),
                                      ('Show As', handler)))

    printmenu = menu.create_menu(label='Print')
    menu.create_menu(printmenu, label='Print Submenu', options=(('Print', handler),
                                        ('Print Now', handler)))
    menu.add_options(printmenu, (('Publish Now', handler),))

    root.title('Menu')
    root.mainloop()

if __name__ == '__main__': testFrameWork()

