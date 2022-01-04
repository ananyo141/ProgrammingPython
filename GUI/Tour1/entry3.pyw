from tkinter import *
from quitter import Quitter
from entry2  import fields


def fetch(entvars: [StringVar]) -> None:
    #try(entvars[0].
    for ent in entvars:
        print(ent.get())

def makeform(parent:Toplevel = None) -> [StringVar]:
    packconfig = dict(
        expand=True,
        fill=BOTH,
    )

    root = Frame(parent)
    root.pack(**packconfig)
    entfields = []
    for field in fields:
        row = Frame(root)
        row.pack(**packconfig)
        Label(row, text=field, width=max(map(len, fields))).pack(side=LEFT, **packconfig)
        fieldVar = StringVar()          # use tkinter string variable class
        entfield = Entry(row, textvariable=fieldVar)
        entfield.pack(side=RIGHT, **packconfig)
        fieldVar.set('Enter here')
        entfields.append(fieldVar)
    return entfields

    
def ask(parent:Toplevel = None) -> None:
    popup = Toplevel(parent)
    popup.maxsize(240, 100)
    popup.minsize(200, 80)
    entryVars = makeform(popup)
    Button(popup, text='Fetch', command=lambda: fetch(entryVars)).pack(side=LEFT, expand=True)
    Quitter(popup).pack(side=RIGHT , expand=True)
    popup.bind('<Return>', lambda event: fetch(entryVars))
    # make modal popup
    popup.focus_set()
    popup.grab_set()
    popup.wait_window()
    

if __name__ == '__main__':
    root = Tk()
    Button(root, text='Input', height=2, width=10, command=lambda: ask(root)).pack(expand=True, fill=X)
    Button(root, text='Quit', command=root.quit).pack(expand=True)
    mainloop()

