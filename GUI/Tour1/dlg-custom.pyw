import sys
from tkinter import *

makemodal = len(sys.argv) > 1
title = 'Modal' if makemodal else 'Non-Modal'

def makePopup():
    popupDiag = Toplevel(root)
    popupDiag.title(title)
    Button(popupDiag, text='OK', command=popupDiag.destroy).pack()
    if makemodal:
        popupDiag.focus_set()
        popupDiag.grab_set()
        popupDiag.wait_window()

root = Tk()
root.title(title + ' Custom Dialog')
root.geometry("330x30")
Button(root, text='popup', command=makePopup).pack(expand=True, fill=BOTH)
mainloop()

