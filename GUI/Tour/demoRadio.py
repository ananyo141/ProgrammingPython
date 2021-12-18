from tkinter import *
from quitter import Quitter
from dialogTable import demos

class Demo(Frame):
    buttonconfig = dict(
        expand=True,
        fill=BOTH,
    )

    def __init__(self, parent=None, radiobuttons=list(demos.keys()), **kw):
        Frame.__init__(self, parent, **kw)
        self.pack()
        self.makebuttons()
        Label(self, text='Radio demos').pack(**self.buttonconfig)
        self.makeradios(radiobuttons)
    
    def makeradios(self, buttonlist):
        self.radiovar = StringVar()
        self.radiovar.set(' ')
        for button in buttonlist:
            Radiobutton(self, text=button,
                              command=self.onPress,
                              variable=self.radiovar,
                              value=button).pack(anchor=NW)

    def makebuttons(self):
        config = dict(
            expand=True,
            fill=X,
            side=BOTTOM,
        )
        Quitter(self).pack(**config)
        Button(self, text='State', command=self.report).pack(**config)

    def report(self):
        print(self.radiovar.get())
    
    def onPress(self):
        action = self.radiovar.get()
        if action in demos:
            print(demos[action]())
        else:
            print('Not implemented')

if __name__ == '__main__':
    Demo().mainloop()

