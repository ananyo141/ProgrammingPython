from tkinter import *
from multiprocessing import Process
from importlib import import_module

demoMods = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']

def makeWin(parent=None, module=None):
    if module is None:
        raise Exception("Module not specified")
    parent = Tk() if parent is None else parent
    popup = Toplevel(parent)
    import_module(module).Demo(popup).pack()
    popup.mainloop()


if __name__ == '__main__':
    root = Tk()
    Message(root, text='GUI in different processes',
            fg='red', bg='white',
    ).pack()
    for module in demoMods:
        (Process(target=makeWin, args=(None, module))).start()

