# A reusable quit button

from tkinter import *
from tkinter.messagebox import askokcancel

class Quitter(Frame):
    def __init__(self, parent=None, **kwargs):
        Frame.__init__(self, parent, **kwargs)
        self.pack()         # repack at convenience
        widget = Button(self, text='Quit', command=self.quitCallback)
        widget.pack(side=RIGHT, expand=YES, fill=BOTH)

    def quitCallback(self):
        ans = askokcancel('Confirm?', 'Are you sure you want to quit?')
        if ans: Frame.quit(self)

if __name__ == '__main__': Quitter().mainloop()

