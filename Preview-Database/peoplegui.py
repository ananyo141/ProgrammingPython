"""Implement a GUI for viewing and updating records from shelve"""

from tkinter import *
from tkinter.messagebox import showerror
import shelve

shelvename = 'class-shelve.auto'
fieldnames = ('name', 'age', 'job', 'pay')

def makeWidgets():
    global entries
    window = Tk()   # make main window to host buttons and input fields
    window.title('People Shelve')
    form = Frame(window) # host the buttons
    form.pack()
    entries = {}    # make entries global
    for (index, label) in enumerate(('key',) + fieldnames):
        lab = Label(form, text = label)
        ent = Entry(form)
        lab.grid(row = index, column = 0)
        ent.grid(row = index, column = 1)
        entries[label] = ent
    Button(window, text = 'Fetch',  command = fetchRecord).pack(side = LEFT)
    Button(window, text = 'Update', command = updateRecord).pack(side = LEFT)
    Button(window, text = 'Quit',   command = window.quit).pack(side = RIGHT)
    return window

def fetchRecord():
    key = entries['key'].get()
    try:
        record = db[key]        # fetch by key, show in GUI
    except:
        showerror(title = 'Error', message = 'No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))

def updateRecord():
    key = entries['key'].get()
    if key in db:
        record = db[key]            # update existing record
    else:
        from person import Person   # make new person
        record = Person(name = '?', age = '?')
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record

db = shelve.open(shelvename)
window = makeWidgets()
window.mainloop()
db.close()
