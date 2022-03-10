import os
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showerror, askyesno

"""
NOTE: This module is not written with optimisation and safety in mind.
It uses blatant eval call that runs client code unobstructed, and instead
of calculating rows and columns and adjusting entry widgets in `entries` (list
of entry widgets) per load, deletes all entry widgets and the label sum
variables and creates them all anew. Not only is this inefficient but also
unnecessary.

Also this is not thoroughly tested, it seems to retain some phantom (empty)
grids, similar bugs may arise upon further testing.

"""

class SummerGrid(Frame):
    signature = 'Signed by: ' + os.path.basename(__file__)

    def __init__(self, parent=None, rows=5, cols=4, **kw):
        Frame.__init__(self, parent, **kw)
        self.entries = []
        self.sumVars = []
        self.makeMenu()
        self.makeEntries(rows, cols)    # set self rows and cols
        self.makeSumFields()

    def makeEntries(self, 
                    rows=None, 
                    cols=None, 
                    matrix=[[i+1 for i in range(5)] for j in range(5)]):
        " Create the matrix as a grid of entry widgets "
        if rows is None: rows = len(matrix)
        cols = 0 if not rows else len(matrix[0])

        self.rows, self.cols = rows, cols
        for rowNum in range(self.rows):
            col = []
            for colNum in range(self.cols):
                ent = Entry(self)
                ent.insert('0', matrix[rowNum][colNum])
                ent.grid(row=rowNum, column=colNum, sticky=NSEW)
                ent.bind('<Button-3>', self.onRightClick)
                col.append(ent)
                self.columnconfigure(colNum, weight=1)
            self.entries.append(tuple(col))
            self.rowconfigure(rowNum, weight=1)

        self.makeSumFields()

    def clearEntries(self):
        " Destroy the entry widgets "
        for entryCol in self.entries:
            for entry in entryCol:
                entry.destroy()
        self.rows = self.cols = 0
        self.entries.clear()

    def makeSumFields(self):
        for var in self.sumVars: del(var)
        self.sumVars.clear()
        for colNum in range(self.cols):
            var = StringVar(value='?')
            Label(self, textvariable=var).grid(row=self.rows, column=colNum, sticky=EW)
            # Column is already expandable due to prev call at make entries
            self.sumVars.append(var)

    def makeMenu(self):
        menu = Menu(self, tearoff=False)
        menu.add_command(label='Sum',   command=self.onSum,   underline=0)
        menu.add_command(label='Print', command=self.onPrint, underline=0)
        menu.add_command(label='Clear', command=self.onClear, underline=0)

        toolMenu = Menu(menu, tearoff=False)
        menu.add_cascade(label='Tools', menu=toolMenu, underline=0)
        toolMenu.add_command(label='Dump', command=self.onDump, underline=0)
        toolMenu.add_command(label='Load', command=self.onLoad, underline=0)
        menu.add_separator()
        menu.add_command(label='Quit',  command=self.onQuit, underline=0)

        self.menu = menu

    def onRightClick(self, event):
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    def onSum(self):
        for i in range(self.cols):
            colSum = 0
            for j in range(self.rows):
                try:
                    colSum += eval(self.entries[j][i].get())
                except: pass
            self.sumVars[i].set(colSum)

    def onPrint(self):
        for entryColumn in self.entries:
            for entry in entryColumn:
                print(repr(entry.get()), end=' ')
            print()
        print()

    def onClear(self):
        for entryColumn in self.entries:
            for entry in entryColumn:
                entry.delete('0', END)

    def onDump(self):
        initialfile = os.path.splitext(__file__)[0]
        savefilename = asksaveasfilename(title='Enter dump file',
                initialfile=initialfile, defaultextension='.dat',
                filetypes=(('Data file', '*.dat'), ('All', '*')))
        if not savefilename: return
        with open(savefilename, 'w') as savefile:
            savefile.write(self.signature + '\n')
            for entryColumn in self.entries:
                for entry in entryColumn:
                    savefile.write(entry.get() + ' ')
                savefile.write('\n')

    def onLoad(self):
        # Commentary: On retrospect, usual try except, if else cascades were
        # better...
        def checkReadable():
            try:
                return open(filename).readlines()
            except:
                showerror(title='Invalid File',
                        message='Unable to read file')
        def checkNotEmpty():
            if len(filelines) == 0:
                showerror(title='Empty File', message='File is empty')
                return False
            return True
        def checkSignature():
            if filelines[0].strip() != self.signature:
                showerror(title='Invalid File',
                          message="File signature doesn't match. Are you sure "
                                  "this is a valid load file?")
                return False
            return True

        filename = askopenfilename(title='Enter load file',
                filetypes=(('Data file', '*.dat'), ('All', '*')))
        if filename and (filelines := checkReadable()) and \
                checkNotEmpty() and checkSignature():
            self.clearEntries()
            loadMatrix = [line.strip().split(' ') for line in filelines[1:]]
            self.makeEntries(matrix=loadMatrix)

    def onQuit(self):
        import sys
        askyesno(title='Confirmation', 
                 message='Are you sure you want to quit?') and sys.exit(0)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('ROWS', nargs='?', help='Number of Rows', default=5, type=int)
    parser.add_argument('COLS', nargs='?', help='Number of Cols', default=5, type=int)
    args = parser.parse_args()

    root = Tk()
    SummerGrid(root, rows=args.ROWS, cols=args.COLS).pack(expand=True, fill=BOTH)
    mainloop()

