from tkinter import *
from tkinter.colorchooser import askcolor

class ShiftColor(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, **kw)
        self.pack(expand=True, fill=BOTH)
        self.makewidgets()
    
    def makewidgets(self):
        widget = Label(self, font=('times', 15, 'bold'), text="Set Background Color!")
        widget.pack(expand=True, fill=BOTH)
        Button(self, text="Choose Color",
               command=lambda: self.changeLabelBg(widget)).pack(side=BOTTOM, fill=X)

    def changeLabelBg(self, widget):
        rgb, hexstr = askcolor()
        if hexstr: widget.config(bg=hexstr)

if __name__ == '__main__': 
    root = Tk()
    root.title("Color Changer")
    root.geometry("300x250")
    ShiftColor(root).mainloop()

