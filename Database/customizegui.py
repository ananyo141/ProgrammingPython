from tkinter import *
from tkinter.messagebox import showinfo
from tkinter102 import MyGui

class CustomGui(MyGui):
    # this changes my class to customize the event function
    def reply(self):
        showinfo(title = 'Pop Window', message = "Ouch!")

if __name__ == '__main__':
    CustomGui().pack()
    mainloop()
