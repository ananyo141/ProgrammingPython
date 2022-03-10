from tkinter import *

class Alarm(Frame):
    def __init__(self, master=None, msecs=1000):
        Frame.__init__(self, master)
        self.msecs = msecs
        self.button = Button(self, text='Quit', width=5, command=self.quit)
        self.button.config(bg='navy', fg='white', bd=9)
        self.button.pack(expand=True, fill=BOTH)
        self.repeater()

    def repeater(self):
        self.bell()
        self.button.flash()
        self.after(self.msecs, self.repeater)

if __name__ == '__main__':
    Alarm().pack()
    mainloop()

