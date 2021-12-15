from tkinter import *
from tkinter.messagebox import *

def quitCallback():
    if askyesno('Verify', 'Do you really want to quit?'):
        showerror('Error', 'Quit not implemented')
    else:
        showinfo('Aborted', 'Quit cancelled')

packKwargs = dict(
    side=TOP,
    expand=True,
    fill=X,
    padx=5,
    pady=2
)

dims = dict (
    height=2,
    width=30
)

errmsg = "Please don't spam"
root = Tk()
root.title('Dialogs')
frame = Frame(root)
frame.pack(expand=True, fill=BOTH)
Button(frame, text='Quit', command=quitCallback, **dims).pack(**packKwargs)
Button(frame, text='Spam', command=lambda: showwarning('No Spam!', errmsg), **dims).pack(**packKwargs)
mainloop()

