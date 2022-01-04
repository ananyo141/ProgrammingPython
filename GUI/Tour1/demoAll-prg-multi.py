from tkinter import *
from multiprocessing import Process
from importlib import import_module

demoMods = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']

def makeWin(parent=None, module=None):
    if module is None:
        raise Exception("Module not specified")
    import_module(module).Demo(parent).mainloop()

if __name__ == '__main__':
    for module in demoMods:
        Process(target=makeWin, args=(None, module)).start()

    root = Tk()
    Message(root, text='GUI in different processes',
            fg='red', bg='white',
    ).pack()
    root.mainloop()

