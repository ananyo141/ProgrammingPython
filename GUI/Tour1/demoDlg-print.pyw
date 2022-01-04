from tkinter import *
from dialogTable import demos
from quitter import Quitter

class Demos(Frame):
    buttonPacking = dict(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=2,
    )

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, **kw)
        self.pack(expand=True, fill=BOTH)
        self.makewidgets()
    
    def makewidgets(self):
        Quitter(self).pack(side=BOTTOM, **self.buttonPacking)       # priority order-packing
        for key, val in demos.items():
            Button(self, text=key, command = (lambda button=key:    # scope and arg retention
                        self.buttonCallback(button))).pack(**self.buttonPacking)

    def buttonCallback(self, button):
        print(button, '=> ', demos[button]())

if __name__ == '__main__': 
    root = Tk(className = "Dialogs")
    root.geometry("230x200")
    Demos(root).pack()
    mainloop()

