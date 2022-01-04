from tkinter import *
from quitter import Quitter

def fetch(entwidget):
    print(f"Got: {entwidget.get()}")
    entwidget.delete(0, END)
    entwidget.insert(0, 'Insert next')
    entwidget.master.focus()

if __name__ == '__main__':
    root = Tk()
    root.title('EntryDialog')
    entfield = Entry(root)
    entfield.config(width=50)
    entfield.insert(0, 'Insert text here')
    entfield.bind('<FocusIn>', lambda event: entfield.delete(0, END))
    entfield.bind('<Return>',  lambda event: fetch(entfield))
    entfield.pack(expand=True, fill=X)
    Button(root, text='Fetch', command=lambda: fetch(entfield)).pack(side=LEFT, expand=True)
    Quitter(root).pack(side=RIGHT, expand=True)
    mainloop()

