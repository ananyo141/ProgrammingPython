# Automate form construction
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def makeFormRow(parent, 
                label: str, 
                width: int = 15, 
                browse: bool = True,
                save: bool = False,
                extend: bool = False) -> StringVar:
    """
    Make a form entry in the parent widget
    Browse creates a browse button to enter a filename
    Extend allows multiple filenames to be entered
    """
    row = Frame(parent)
    row.pack(fill=X, expand=True)
    Label(row, text=label, width=width, relief=RIDGE).pack(side=LEFT)
    var = StringVar()
    Entry(row, textvariable=var, relief=SUNKEN).pack(side=LEFT, expand=True, fill=X, padx=5)
    if browse:
        getfilename = asksaveasfilename if save else askopenfilename
        handler = ( (lambda: var.set(getfilename() or var.get()))  # get one filename
                  if not extend else
                  (lambda: var.set(getfilename() + ', ' + var.get())) ) # get multiple
        Button(row, text='Browse', command=handler).pack(side=RIGHT)
    return var

