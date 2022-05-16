from tkinter import *
from tkinter.messagebox import showinfo
from importlib import reload
import radactions

class ReloadTest(Tk):
    def __init__(self, *args, **kw):
        Tk.__init__(self, *args, **kw)
        self.makebuttons()

    def makebuttons(self):
        Button(self, text='Text 1', command=self.message1).pack()
        Button(self, text='Text 2', command=self.message2).pack()

    def message1(self):
        reload(radactions)
        radactions.message1(self)

    def message2(self):
        reload(radactions)
        radactions.message2(self)

    def message3(self):
        showinfo(title='Instance Method', message='Hello there from ' + \
                self.__class__.__name__ + ' instance')

if __name__ == '__main__':
    ReloadTest().mainloop()

