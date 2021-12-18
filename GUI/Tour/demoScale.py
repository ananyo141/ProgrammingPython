from tkinter import *
from quitter import Quitter

class Demo(Frame):
    basecfg = dict(
        expand=True,
        fill=BOTH,
    )
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, **kw)
        self.pack()
        self.makebuttons()
        self.makelabel()
        self.makescales()

    def makelabel(self):
        Label(self, text='Scale Demos', 
              font=('courier', 15, 'italic underline')
        ).pack(**self.basecfg)

    def makescales(self):
        self.scale1 = IntVar()
        self.scale2 = IntVar()
        Scale(self, label='1: Pick demo number',
              from_=0, to=4, variable=self.scale1,
              showvalue=NO, length=100,
              resolution=1, tickinterval=4,
        ).pack(**self.basecfg)
        Scale(self, label='2: Pick demo number',
              from_=10, to=20, variable=self.scale2,
              showvalue=YES, command=self.onMove,
              tickinterval=2, orient='horizontal',
              resolution=2
        ).pack(**self.basecfg)
        
    def makebuttons(self):
        Quitter(self).pack(side=BOTTOM, **self.basecfg)
        Button(self, text='State', 
               command=self.report
        ).pack(side=BOTTOM, **self.basecfg)

    def onMove(self, value):
        print(f"Moved and got: {value}")

    def report(self):
        print(f"Scale1: {self.scale1.get()}, Scale2: {self.scale2.get()}")

if __name__ == '__main__': Demo().mainloop()

