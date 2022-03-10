from tkinter import *

def makeForm(parent):
    formFrm = Frame(parent)
    Label(formFrm, text='Search Key: ', width=20).grid(row=0, column=0, sticky=W)
    Entry(formFrm).grid(row=0, column=1, sticky=EW)
    Button(formFrm, text='Browse').grid(row=0, column=2)

    Label(formFrm, text='Directory: ', width=20).grid(row=1, column=0, sticky=W)
    Entry(formFrm).grid(row=1, column=1, columnspan=2, sticky=EW)

    Label(formFrm, text='Num Images', width=20).grid(row=2, column=0, sticky=W)
    Entry(formFrm).grid(row=2, column=1, columnspan=2, sticky=EW)

    for i in range(3):
        parent.rowconfigure(i, weight=1)
        parent.columnconfigure(i, weight=1)

    return formFrm

if __name__ == '__main__':
    makeForm(Tk()).pack(expand=True, fill=BOTH)
    mainloop()

