from tkinter import *
from tkinter.dialog import Dialog

class OldDialog(Frame):
    def __init__(self, master=None, **kw):
        Frame.__init__(self, master, **kw)
        self.pack()
        Button(self, text="Pop1", command=self.dialog1).pack(side=LEFT)
        Button(self, text="Pop2", command=self.dialog2).pack(side=RIGHT)

    def dialog1(self):
        ans = Dialog(self,
                     title  = "PopUp Dialog",
                     text   = "An example of popup from old dialog",
                     bitmap = "questhead",
                     default=0, strings=("Yes", "No", "Cancel"))
        if ans.num == 0: self.dialog2()

    def dialog2(self):
        ans = Dialog(self,
                     title  = "HAL-9000",
                     text   = "I'm afraid I can't let you do that Dave...",
                     bitmap = "hourglass",
                     default=0, strings=("Intense Stare", "Kubrick STARE"))

if __name__ == '__main__': OldDialog().mainloop()

