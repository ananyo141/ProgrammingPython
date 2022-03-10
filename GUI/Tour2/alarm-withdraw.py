from tkinter import *
from alarm import Alarm

class AlarmWithdraw(Alarm):
    def repeater(self):
        self.bell()
        if self.master.state() == 'normal':
            self.master.withdraw()
        else:
            self.master.deiconify()
            self.master.lift()
        self.after(self.msecs, self.repeater)

if __name__ == '__main__':
    AlarmWithdraw().pack()
    mainloop()

