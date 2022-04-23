# Create a frontend for unpacker.py

from tkinter import *
from formrows import makeFormRow
from unpacker import unpack
from glob import glob
import sys

def createDialog():
    " Spawn dialog to input unpack parameters "
    dialog = Tk()
    dialog.title('Unpacker')
    inputfile = makeFormRow(dialog, 'Input file: ')
    Button(dialog, text='Start', command=dialog.destroy).pack()
    dialog.bind('<Key-Return>', lambda event: dialog.destroy())
    dialog.focus_set()
    dialog.grab_set()
    dialog.wait_window()
    return inputfile.get()

def unpackFromDialog():
    " Take unpack parameter from dialog and run unpack "
    packedfile = createDialog()
    if packedfile:
        try:
            packedfile = glob(packedfile)[0]
        except IndexError:
            sys.exit("No files found")
        unpack(packedfile, prefix='new-')

if __name__ == '__main__': unpackFromDialog()

