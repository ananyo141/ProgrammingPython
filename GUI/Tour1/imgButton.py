from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk
import sys

def getImage():
    imagefilename = askopenfilename(title='Choose image file')
    if not imagefilename: sys.exit('No files chosen')
    return imagefilename

if __name__ == '__main__':
    imagefilename = getImage()
    root = Tk()
    img = ImageTk.PhotoImage(file=imagefilename)
    Button(root, image=img).pack()
    mainloop()

