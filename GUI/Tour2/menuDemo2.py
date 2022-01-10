import os, mimetypes
import tkinter as tk
from tkinter.constants import *
from PIL.ImageTk import Image, PhotoImage
from menuDemo import NewMenuDemo

class ImageToolbar(NewMenuDemo):
    def makewidgets(self):
        self.makemenubar()
        self.maketoolbar()
        tk.Label(self, text='Toolbar With Images',
                 font=('times', 20, 'italic underline'),
                 bd=3, relief=SUNKEN, bg='skyblue', fg='maroon',
                 height=12, width=30,
        ).pack(expand=True, fill=BOTH)

    def maketoolbar(self, toolimgdir=os.curdir, thumbsize=(75,80)):
        self.toolimgdir = toolimgdir
        toolbar = tk.Frame(self)
        toolbar.pack(fill=X)

        self.toolsaveimages = []
        for filename in os.listdir(self.toolimgdir):
            filepath = os.path.join(self.toolimgdir, filename)
            ftype, enc = mimetypes.guess_type(filename)
            if ftype and ftype.split('/')[0] == 'image' and enc is None:
                try:
                    imgobj = Image.open(filename)
                    imgobj.thumbnail(thumbsize, Image.ANTIALIAS)
                    thumb = PhotoImage(imgobj)
                except: continue
                tk.Button(toolbar, text=filename, 
                          height=thumbsize[0], width=thumbsize[1], 
                          bd=2, relief=RIDGE, cursor='hand2',
                          image=thumb, command=self.notdone,
                ).pack(side=LEFT)
                self.toolsaveimages.append(thumb)

if __name__ == '__main__':
    ImageToolbar().mainloop()

