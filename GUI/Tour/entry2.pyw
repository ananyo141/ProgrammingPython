from tkinter import *
from quitter import Quitter
from entry1  import fetch

fields = 'Name', 'Job', 'Pay'

def makefields(parent, fields):
    packconfig = dict(
        expand=True,
        fill=BOTH,
    )

    entfields = []
    mainframe = Frame(parent)
    mainframe.pack(**packconfig)
    for field in fields:
        row = Frame(mainframe)
        row.pack(**packconfig)
        Label(row, width=max(map(len, fields)), text=field).pack(side=LEFT, expand=True)
        entfield = Entry(row)
        entfield.insert(0, 'Insert here')
        entfield.bind('<FocusIn>', lambda event, entfield=entfield:
                                          entfield.delete(0, END))
        entfield.pack(side=RIGHT, padx=5, **packconfig)
        entfields.append(entfield)
    return entfields

def main():
    buttonConfig = dict(
       #expand=True,
        padx=10,
        pady=6,
    )

    root = Tk()
    root.title('Fields')
    root.minsize(200,90)
    root.maxsize(300,150)
    root.geometry("250x100")
    entries = makefields(root, fields)
    Button(root, text='Fetch', command=(lambda: list(fetch(ent) for ent in entries))).pack(side=LEFT,
                                                                                      **buttonConfig)
    root.bind('<Return>', lambda event: list(map(fetch, entries)))
    Quitter(root).pack(side=RIGHT, **buttonConfig)
    mainloop()
    
if __name__ == '__main__': main()

