from tkinter import *
from dialogTable import demos
from quitter import Quitter

class Demo(Frame):
    def __init__(self, parent=None, message=None, **kw):
        Frame.__init__(self, parent, **kw)
        self.pack(expand=True, fill=BOTH)
        self.attachbuttons()
        self.makelabel(message)
        self.makechecks()

    def makelabel(self, message):
        Label(self, text=message).pack(expand=True, fill=BOTH)

    def makechecks(self):
        self.vars = []
        for key in demos:
            var = IntVar()
            Checkbutton(self, text=key, 
                              variable=var,
                              command=demos[key]).pack(side=LEFT, 
                              expand=True, anchor=W)
            self.vars.append(var)

    def attachbuttons(self):
        buttonconfig = dict(
            expand=True,
            fill=BOTH,
        )
        (buttonFrame := Frame(self)).pack(side=RIGHT, **buttonconfig)
        Quitter(buttonFrame).pack(**buttonconfig)
        Button(buttonFrame, text='State', command=self.report).pack(**buttonconfig)

    def report(self):
        for var in self.vars:
            print(var.get(), end=' ')
        print()
            

if __name__ == '__main__': Demo(message='Demo Check').mainloop()

