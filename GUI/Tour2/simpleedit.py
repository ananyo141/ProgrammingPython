import tkinter as tk, sys
from tkinter import ttk, messagebox, filedialog, simpledialog
from scrolltext import ScrollText

class SimpleEdit(ScrollText):
    filetypes = (('Text',          '.txt'),
                 ('Python Scripts', '.py'),
                 ('C Source',        '.c'),
                 ('CPP Source',    '.cpp'),
                 ('All',            '*.*'))

    def __init__(self, parent=None, text='', file=None, **kw):     # Attach to toplevel
        ScrollText.__init__(self, parent, text, file, **kw)        # as it configures menu
        self.prevSearch = None
        self.makemenu()
        self.master.protocol('WM_DELETE_WINDOW', self.quit)

    def makemenu(self):
        self.menubar = tk.Menu(self.master)
        self.master.config(menu=self.menubar)

        file = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label='File', menu=file,       underline=0)
        file.add_command(label='Open',    command=self.opennew, underline=0)
        file.add_command(label='Save As', command=self.saveas,  underline=0)
        file.add_separator()
        file.add_command(label='Quit',    command=self.quit,    underline=0)

        edit = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label='Edit', menu=edit,   underline=0)
        edit.add_command(label='Cut',   command=self.cut,   underline=0)
        edit.add_command(label='Paste', command=self.paste, underline=0)

        options = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label='Options', menu=options,    underline=0)
        options.add_command(label='Find',    command=self.find,    underline=0)
        options.add_command(label='Replace', command=self.replace, underline=0)

    def opennew(self):
        file = tk.filedialog.askopenfilename(title='Open New', filetypes=self.filetypes)
        if file: self.settext(file=file)

    def saveas(self):
        savefile = tk.filedialog.asksaveasfilename(title='Save As', filetypes=self.filetypes,
                        initialfile='Untitled-SimpleEdit', defaultextension=('Text', '.txt'))
        if savefile:
            text = self.textwid.get('1.0', 'end')
            open(savefile, 'w').write(text)

    def cut(self):
        textSelected = self.textwid.get('sel.first', 'sel.last')
        self.clipboard_clear()
        self.clipboard_append(textSelected)
        self.textwid.delete('sel.first', 'sel.last')
        
    def paste(self):
        try:
            topaste = self.selection_get(selection='CLIPBOARD')
            self.textwid.insert('insert', topaste)
        except TclError: 
            tk.messagebox.showerror('Paste Error', 'Clipboard Empty')

    def find(self):
        searchstr = tk.simpledialog.askstring('Find', 
                        'Enter target', initialvalue=self.prevSearch)
        self.prevSearch = searchstr
        if not searchstr: return

        index = self.textwid.search(searchstr, 'insert', 'end')
        if index:
            pastIt = f'{index}+{len(searchstr)}c'
            self.textwid.tag_add('sel', index, pastIt)
            self.textwid.mark_set('insert', pastIt)
            self.textwid.see('insert')
            self.textwid.focus()
        else:
            tk.messagebox.showerror('Not Found', f"{repr(searchstr)} can't be found")

    def replace(self):
        popup = tk.Toplevel(self)
        popup.title('Replace')
        popup.maxsize(300, 110)
        popup.minsize(250, 95)
        fieldWidth = max(map(len, ('find: ', 'replace: ')))
        (findFrame    := ttk.Frame(popup)).pack(padx=7)
        (replaceFrame := ttk.Frame(popup)).pack(padx=7)
        ttk.Label(findFrame, text='Find: ',       width=fieldWidth).pack(side='left')
        ttk.Label(replaceFrame, text='Replace: ', width=fieldWidth).pack(side='left')
        (findEnt    := ttk.Entry(findFrame,    width=50)).pack(side='left', padx=6, pady=3)
        (replaceEnt := ttk.Entry(replaceFrame, width=50)).pack(side='left', padx=6, pady=3)

            
        def replaceHandler():
            # Perform search and replace
            findStr    = findEnt.get()
            replaceStr = replaceEnt.get()
            self.prevSearch = findStr
            if ind := self.textwid.search(findStr, 'insert', 'end'):
                self.textwid.delete(ind, f'{ind}+{len(findStr)}c')
                self.textwid.insert(ind, replaceStr)
                pastIt = f'{ind}+{len(replaceStr)}c'
                self.textwid.tag_add('sel', ind, pastIt)
                self.textwid.mark_set('insert', pastIt)
                self.textwid.see('insert')
            else:
                tk.messagebox.showerror('Not found', f"{repr(findStr)} not found")

        ttk.Button(popup, text='Go', command=replaceHandler).pack(pady=6)
        # make modal
        popup.focus_set()
        popup.grab_set()

        # insert if previously searched or replaced
        if self.prevSearch:
            findEnt.insert(0, self.prevSearch)
            replaceEnt.focus()
        else: 
            findEnt.focus()
        # wait for window to close
        popup.wait_window()

    def quit(self):
        tk.messagebox.askokcancel('Quit',
            'Any unsaved changes will be lost. Are you sure?') and sys.exit()

if __name__ == '__main__':
    root = tk.Tk()
    root.title('SimpleEdit')
    SimpleEdit(root).mainloop()

