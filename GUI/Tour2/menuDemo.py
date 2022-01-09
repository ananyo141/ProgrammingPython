import os, mimetypes
import tkinter as tk
from tkinter.constants import *
from tkinter import messagebox
from PIL import Image
from PIL.ImageTk import PhotoImage

class NewMenuDemo(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.pack(expand=True, fill=BOTH)
        self.makewidgets()

    def makewidgets(self):
        self.makemenubar()
        self.maketoolbar()
        tk.Label(self, text='Menu and Toolbar Demo',
                 font=('adwaita', 20, 'bold italic'),
                 bd=3, relief=RAISED, bg='beige', fg='red',
                 height=8, width=30,
        ).pack(expand=True, fill=BOTH)
        
    def makemenubar(self):
        self.menubar = tk.Menu(self.master) # attach to toplevel widgets
        self.master.config(menu=self.menubar)
        self.filemenu()
        self.editmenu()
        self.imagemenu()

    def notdone(self):
        tk.messagebox.showerror('Not Implemented', 'This feature is not implemented')

    def filemenu(self):
        file = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label='File', menu=file,    underline=0)
        file.add_command(label='Open', command=self.notdone, underline=0)
        file.add_command(label='Quit', command=self.quit,    underline=0)

    def editmenu(self):
        edit = tk.Menu(self.menubar)
        self.menubar.add_cascade(label='Edit', menu=edit, underline=0)
        edit.add_command(label='Paste', command=self.notdone)
        edit.add_command(label='Spam',  command=self.notdone)
        edit.add_separator()                        # CHECK ME AFTER RUNNING
        edit.add_command(label='Delete')
        edit.entryconfig(4, state=DISABLED)

    def imagemenu(self, imgdir=os.curdir):
        self.imgdir = imgdir
        self.saveimages = []
        thumbsize = (60,80)

        imagemenu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label='Image', menu=imagemenu, underline=0)
        for filename in os.listdir(self.imgdir):
            ftype, enc = mimetypes.guess_type(filename)
            if ftype and ftype.split('/')[0] == 'image' and enc is None:
                try:
                    photo = Image.open(filename)
                    photo.thumbnail(thumbsize, Image.ANTIALIAS)
                    thumb = PhotoImage(photo)
                except: continue  # if pillow fails to load image
                imagemenu.add_command(label=os.path.basename(filename), 
                                      image=thumb, command=None)
                self.saveimages.append(thumb)

    def maketoolbar(self):
        toolbar = tk.Frame(self)
        toolbar.pack(fill=X)
        tk.Button(toolbar, text='Hello', relief=RAISED, command=(lambda: 
                    tk.messagebox.showinfo('Greetings', 'Hello There!'))
        ).pack(side=LEFT)
        tk.Button(toolbar, text='Quit', command=self.quit,
                  relief=RAISED,
        ).pack(side=RIGHT)
        
if __name__ == '__main__': NewMenuDemo().mainloop()

