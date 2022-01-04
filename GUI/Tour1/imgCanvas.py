from tkinter import *
from PIL import ImageTk
from imgButton import getImage

imagefilename = getImage()
root = Tk()
img = ImageTk.PhotoImage(file=imagefilename)
can = Canvas(root)
can.pack(fill=BOTH)
can.config(width=img.width(), height=img.height())
can.create_image(0, 0, image=img, anchor=NW)
mainloop()

