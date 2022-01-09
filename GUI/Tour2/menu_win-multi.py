import tkinter as tk
from tkinter.constants import *
from menuframework import MakeMenuWin

root = tk.Tk()

for i in range(3):
    win = tk.Toplevel(root)
    win.title('Toplevel: #' + str(i+1))
    menuObj = MakeMenuWin(win)
    menuObj.create_menu(label='File', options=(('New', None),
                                               ('Open', None),
                                               ('Quit', win.destroy)))
    edit = menuObj.create_menu(label='Edit', options=(('Cut', None), ('Paste', None)))
    menuObj.create_menu(menu=edit, label='Stuff', options=(('Spam', None), ('Eggs', None)))
    tk.Label(win, text='Multiple Windows', fg='white', 
             bg='black', height=7, width=35
    ).pack(expand=True, fill=BOTH)

tk.Button(root, text='Bye',
          height=2, width=35,
          command=root.quit).pack(expand=True, fill=BOTH)
root.title('Main Window')
root.mainloop()

