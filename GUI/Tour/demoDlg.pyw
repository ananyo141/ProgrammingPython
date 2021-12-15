from tkinter import *
from dialogTable import demos
from quitter import Quitter

class Demo(Frame):
    buttonPacks = dict(
        expand=True,
        fill=BOTH,
        padx=20,
        pady=2,
    )

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, **kw)
        self.pack(expand=True, fill=BOTH)
        Quitter(self).pack(side=BOTTOM, **self.buttonPacks)
        Label(self, text='Basic Demos').pack(expand=True)
        for demo, action in demos.items():
            Button(self, text=demo, command=action).pack(**self.buttonPacks)

if __name__ == '__main__': Demo().mainloop()

