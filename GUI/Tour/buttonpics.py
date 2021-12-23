from tkinter import *
from PIL import ImageTk
from demoCheck import Demo
import os, glob, random

class ButtonPicsDemo(Frame):
    def __init__(self, parent=None, directory=os.getcwd(), **kw):
        Frame.__init__(self, parent, **kw)
        self.pack(expand=True, fill=BOTH)
        self.directory = directory
        # create image objects to chose from
        files = glob.glob(os.path.join(directory, '*.jpg'))
        self.images = [(x, ImageTk.PhotoImage(file=x)) for x in files]
        self.makelabel()
        self.makebutton()

    def makelabel(self):
        self.lab = Label(self, text='none', bg='white', fg='blue')
        self.lab.pack(fill=BOTH)

    def makebutton(self):
        self.button = Button(self, text='click me', command=self.cycle)
        self.button.pack(expand=True, fill=BOTH)

    def cycle(self):
        name, img = random.choice(self.images)
        self.lab.config(text=name)
        self.button.config(image=img)
        

if __name__ == '__main__': 
    from tkinter.filedialog import askdirectory
    dirname = askdirectory(title='Photo Folder')
    dirname = os.path.normpath(dirname) if dirname is not None else quit()
    root = Tk()
    root.title('Button Pics')
    ButtonPicsDemo(root, directory=dirname).mainloop()

