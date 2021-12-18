from tkinter import *
from importlib import import_module
from quitter import Quitter

demoMods = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']

def makeWin(modules, parent=None):
    objs = []
    for modname in modules:
        try:
            mod = import_module(modname)
        except ModuleNotFoundError:
            print(f"{mod} not found. Skipping...")
            continue
        top = Toplevel()
        obj = mod.Demo(top)
        top.title(mod.__name__)
        objs.append(obj)
    return objs

def reportStates(objs):
    for obj in objs:
        if hasattr(obj, 'report'):
            print(obj.__module__, '=>', obj.report())

if __name__ == '__main__':
    def spawnwin(parent):
        global winobjs
        winobjs = makeWin(demoMods, parent)

    buttoncfg = dict(
        expand=True,
        padx=3,
        pady=3,
        anchor=S
    )
    root = Tk()
    root.title('Popups')
    Button(root, text='Make Windows',
           command=lambda: spawnwin(root)
    ).pack(**buttoncfg)
    Button(root, text='States',
           command=lambda: reportStates(winobjs)
    ).pack(**buttoncfg)
    Quitter(root).pack(**buttoncfg)
    mainloop()

