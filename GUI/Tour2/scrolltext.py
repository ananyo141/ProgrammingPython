import tkinter as tk
from tkinter import messagebox

class ScrollText(tk.Frame):
    def __init__(self, parent=None, text='', file=None, **kw):
        tk.Frame.__init__(self, parent, **kw)
        self.makewidgets()
        self.settext(text, file)
        self.pack(expand=True, fill='both')

    def makewidgets(self):
        textwid = tk.Text(self, relief='groove', font=('courier', 14, 'italic'))

        yscroll = tk.Scrollbar(self, command=textwid.yview)
        xscroll = tk.Scrollbar(self, command=textwid.xview, orient='horizontal')
        textwid.config(yscrollcommand=yscroll.set)
        textwid.config(xscrollcommand=xscroll.set)

        yscroll.pack(side='right',  fill='y')
        xscroll.pack(side='bottom', fill='x')
        textwid.pack(expand=True,   fill='both')

        self.textwid = textwid  # save a reference
        self.bindwidgets()
    
    def bindwidgets(self):
        self.textwid.bind('<Key-Escape>', self.report)

    def settext(self, text='', file=None):
        text = text if file is None else open(file, 'r').read()
        self.textwid.delete('1.0', 'end')
        self.textwid.insert('1.0', text)
        self.textwid.mark_set('insert', '1.0')
        self.textwid.focus()

    def gettext(self):
        return self.textwid.get('1.0', 'end-1c')

    def report(self, event):
        tk.messagebox.showinfo('Report', self.gettext())
        self.textwid.mark_set('insert', '1.0')
        self.textwid.tag_add('sel', '1.0', 'end-1c')

if __name__ == '__main__':
    import sys
    file = None if len(sys.argv) < 2 else sys.argv[1]

    root = tk.Tk()
    root.title('Text')
    ScrollText(root, file=file).mainloop()

