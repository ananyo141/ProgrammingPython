from tkinter import *
from tkinter.messagebox import showinfo

class MyGui(Frame):
    def __init__(self, parent = None):
        Frame.__init__(self, parent)
        self.pressCount = 0         # keep track of number of button presses
        # my class constructor creates a button and a target function for event
        button = Button(self, text = 'press', command = self.reply)
        button.pack()
    def reply(self):
        self.pressCount += 1
        showinfo(title = 'popup', message = f'Button pressed {self.pressCount} times!')

if __name__ == '__main__':
    window = MyGui()
    window2 = MyGui()
    window2.pack()
    window.pack()
    window2.mainloop()
    window.mainloop()
