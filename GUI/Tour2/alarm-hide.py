from tkinter import *
from alarm import Alarm

class AlarmHide(Alarm):
    def __init__(self, *args, **kw):
        self.shown = False
        Alarm.__init__(self, *args, **kw)

    def repeater(self):
        self.bell()
        if self.shown:
            self.button.pack_forget()
        else:
            self.button.pack()
        self.shown = not self.shown
        self.after(self.msecs, self.repeater)

if __name__ == '__main__':
    AlarmHide().pack()
    mainloop()

