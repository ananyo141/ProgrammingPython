"""
A Mixin class with utility methods intended to be 'mixed' with
client subclasses
"""

import os
import tkinter as tk
import tkinter.messagebox as msgb
import tkinter.filedialog as fldg

# Mixin Methods
class GuiMixin:
    # Infobox
    def infobox(self, title='Info', message=''):
        return msgb.showinfo(title, message)

    # errorbox
    def errorbox(self, message=''):
        msgb.showerror('Error!', message)

    # question
    def question(self, title='Question?', message=''):
        return msgb.askyesno(title, message)

    # notdone
    def notimplemented(self, message='This feature is not yet implemented'):
        msgb.showwarning('Not Implemented!', message)

    def confirmation(self):
        return msgb.askyesno('Sure?', 'Are you sure?')

    # quit
    def quit(self):
        msgb.askyesno('Confirm?', 'Are you sure you want to quit?') and \
            tk.Frame.quit(self)     # must be mixed with Frame class to use quit

    # help
    def help(self):
        self.infobox('Help', 'Show help message') # redefine me

    # selectopenfile
    def selectOpenFile(self, initialfile='', initialdir=os.curdir,
                filetypes=[('All', '*')]):
        return fldg.askopenfilename(initialfile=initialfile, initialdir=initialdir,
                filetypes=filetypes)

    # selectopenfile
    def selectSaveFile(self, initialfile='', initialdir=os.curdir,
                defaultextension='', filetypes=[('All', '*')]):
        return fldg.asksaveasfilename(initialfile=initialfile, initialdir=initialdir,
                filetypes=filetypes, defaultextension=defaultextension)    # selectsavefile

    # clone
    def clone(self, *args):
        " create a new instance of lowest derived class in a new window "
        new = tk.Toplevel()
        cls = self.__class__
        cls(new, *args)

    # spawn
    def spawn(self, pycmdline, wait=False):
        from subprocess import Popen
        assert isinstance(pycmdline, (tuple, list)), \
            "Should be either a list or tuple"
        childproc = Popen(args=pycmdline)
        if wait: childproc.wait()

    # browser
    def browser(self, filename):
        from tkinter.scrolledtext import ScrolledText
        new = tk.Toplevel()
        stwidget = ScrolledText(new)
        stwidget.config(width=60, height=25, 
                font=('courier', 14, 'normal') )
        stwidget.pack(expand=True, fill='both')
        new.title('Text Browser')
        new.iconname('Viewer')
        new.protocol('WM_DELETE_WINDOW', 
                lambda: self.confirmation() and new.destroy())
        stwidget.insert('end', open(filename).read())

if __name__ == '__main__':
    # self test code
    import sys
    class TestMixin(GuiMixin, tk.Frame):
        def __init__(self, master=None, *args, **kw):
            tk.Frame.__init__(self, master, *args, **kw)
            self.pack()
            self.testButtons()

        def testButtons(self):
            tk.Button(self, text='info', command =
                lambda: self.infobox('Info', 'This is the infobox')).pack()
            tk.Button(self, text='error', command =
                lambda: self.errorbox(message='This is error box')).pack()
            tk.Button(self, text='question', command =
                lambda: self.question(message='This is question box')).pack()
            tk.Button(self, text='not done', command=self.notimplemented).pack()
            tk.Button(self, text='help', command=self.help).pack()
            tk.Button(self, text='open', command=self.selectOpenFile).pack()
            tk.Button(self, text='save', command=self.selectSaveFile).pack()
            tk.Button(self, text='clone', command=self.clone).pack()
            tk.Button(self, text='spawn', command =
                    lambda: self.spawn((sys.executable,))).pack()
            tk.Button(self, text='browser', command =
                    lambda: self.browser(self.selectOpenFile())).pack()

    TestMixin().mainloop()

