import os
from tkinter import Frame, Button
from tkinter.filedialog import askopenfilename, asksaveasfilename

class ModalAsker(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(expand=True, fill='both')
        self.savefilename = self.openfilename = None
        Button(self, text='Open', command=self.openfile).pack()
        Button(self, text='Save', command=self.savefile).pack()

    def openfile(self):
        self.openfilename = askopenfilename()

    def savefile(self):
        self.savefilename = asksaveasfilename(initialdir =
                os.path.dirname(__file__))
    
    def show(self):
        print(f'{self.openfilename = }')
        print(f'{self.savefilename = }')

if __name__ == '__main__':

    # World of event driven
    widget = ModalAsker()
    widget.mainloop()

    # back to procedural
    widget.show()

    # again event
    widget = ModalAsker()
    widget.mainloop()

    # end of the show...
    widget.show()

