from tkinter import *
from importlib import import_module
from quitter import Quitter
demoModules = ['demoDlg', 'demoCheck', 'demoRadio', 'demoScale']

def attachFrames(parent=None, demos=[]):
    demoObjs = []
    for demo in demos:
        try:
            demoFrame = import_module(demo).Demo(parent)
        except ModuleNotFoundError:
            from sys import stderr
            print(f'{demo} not found', file=stderr)
            continue
        demoFrame.config(bd=2, relief=GROOVE)
        demoFrame.pack(side=LEFT, expand=True, fill=BOTH)
        demoObjs.append(demoFrame)
    return demoObjs

def printStates(frmObjs):
    print(' All States '.center(50, '*'))
    for obj in frmObjs:
        if hasattr(obj, 'report'):
            print(obj.report())
        else:
            print(f"{obj.__module__} -> None")
    print()

root = Tk()
root.title('Frames')
frameObjs = attachFrames(root, demoModules)
Label(root, text='Multiple Frame demo',
      bg='white', font=('helvetica', 20, 'bold'),
).pack(expand=True, fill=BOTH)
Button(root, text='States', 
       command=lambda: printStates(frameObjs)
).pack(expand=True, fill=BOTH)
mainloop()

