from tkinter import *
import _thread
from guiStreams import redirectedGuiShellCmd

def spawn():
    _thread.start_new_thread(redirectedGuiShellCmd, ('python3 -u socket-nongui.py',))

root = Tk()
Button(root, text='Go!', command=spawn).pack()

mainloop()

