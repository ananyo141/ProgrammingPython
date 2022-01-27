import tkinter as tk
from tkinter.constants import *

class ScrollList(tk.Frame):
    def __init__(self, options, parent=None, **kw):
        tk.Frame.__init__(self, parent, **kw)
        self.pack(expand=True, fill=BOTH)
        self.makewidgets(options)

    def makewidgets(self, options):
        listbox = tk.Listbox(self, relief=SUNKEN)
        ysbar = tk.Scrollbar(self, command=listbox.yview)
        xsbar = tk.Scrollbar(self, command=listbox.xview, orient='horizontal')
        listbox.config(selectmode=MULTIPLE)
        listbox.config(yscrollcommand=ysbar.set)
        listbox.config(xscrollcommand=xsbar.set)

        ysbar.pack(side=RIGHT,  fill=Y)
        xsbar.pack(side=BOTTOM, fill=X)
        listbox.pack(expand=True, fill=BOTH)

        # populate listbox
        for option in options:
            listbox.insert(END, option)
        listbox.bind('<Double-1>', self.listdoubleclick)
        self.listbox = listbox

    def listdoubleclick(self, event):
        option = self.listbox.get(ACTIVE)
        self.runcommand('Clicked: ' + option)
        for selection in self.listbox.curselection():
            selected = self.listbox.get(selection)
            self.runcommand('Selected: ' + selected)

    def runcommand(self, option):
        print(option)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('200x100')
    root.title('List')
    root.iconname('ListScroll')
    options = (('%d: A quick brown fox jumps over the lazy dog' % num) for num in range(1, 31))
    ScrollList(options, root).mainloop()

