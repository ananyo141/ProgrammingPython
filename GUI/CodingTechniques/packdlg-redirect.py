from tkinter import Tk, Button
from packdlg import packFromDialog
from guiStreams import redirectedGuiFunc

def packDlgWrapped():
    redirectedGuiFunc(packFromDialog)

if __name__ == '__main__':
    root = Tk()
    Button(root, text='pop', command=packDlgWrapped).pack(fill='x')
    root.mainloop()

