from tkinter import *

root = Tk()
entries = []

for i in range(5):
    col = []
    for j in range(4):
        (ent := Entry(root, width=3)).grid(row=i, column=j, sticky=NSEW)
        ent.insert(END, '{row}.{col}'.format(row=i, col=j))
        col.append(ent)
        root.columnconfigure(j, weight=1)
    root.rowconfigure(i, weight=1)
    entries.append(col)

def fetch(entries):
    for row in entries:
        for col in row:
            print(col.get(), end=' ')
        print()
    print('\n\n', end='')

Button(root, text='Fetch', command=lambda: fetch(entries)).grid(sticky=EW,
        columnspan=4)
mainloop()

