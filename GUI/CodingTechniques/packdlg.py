# Create a frontend for packer.py

from tkinter import *
from formrows import makeFormRow
from packer import pack
from glob import glob

def createDialog():
    " Gui for pack, return outputfile(str) and inputfiles(str) in tuple "
    dialog = Toplevel()     # use top level widgets instead of Tk() root to avoid
    dialog.title('Packer')  # grab exception in ./packdlg-redirect.py
    outputfile = makeFormRow(dialog, 'Output File: ', save=True)
    inputfiles = makeFormRow(dialog, 'Files to pack: ', extend=True)
    Button(dialog, text='Start', command=dialog.destroy).pack()
    dialog.focus_set()
    dialog.grab_set()
    dialog.wait_window()
    return outputfile.get(), inputfiles.get()

def packFromDialog():
    outfile, inputfiles = createDialog()
    inputfiles = inputfiles.split(', ')[:-1]
    if outfile and inputfiles:
        globbedfiles = []
        for sublist in map(glob, inputfiles):
            globbedfiles += sublist
        pack(outfile, globbedfiles)

if __name__ == '__main__': packFromDialog()

