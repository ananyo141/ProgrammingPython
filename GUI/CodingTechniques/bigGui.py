# Client demo program to use guimaker.py module

import sys
from tkinter import *
from tkinter.ttk import *
from guimixin import GuiMixin
from guimaker import GuiNativeMaker

class ClientTest(GuiMixin, GuiNativeMaker):
    def greeting(self):
        self.hellos += 1
        if self.hellos % 3:
            self.infobox(message='Hello There')
        else:
            print('Hi')

    def dialog(self):
        choice = self.question(message='Are you sure?')
        [lambda: None, self.quit][choice]() # Nothing if false, quit if true

    def more(self):
        win = Toplevel()
        Label(win, text='A new non-modal window').pack(expand=True, fill=BOTH)

    def pickDemo(self):
        demo = self.selectOpenFile(filetypes=[('Python', '*.py')])
        if demo:
            self.spawn((sys.executable, demo))

    def browseSource(self):
        self.browser(__file__)

    def makeWidgets(self):
        Label(self, text= f'This is {self.__class__.__name__}, '
            'hi and welcome to the tour', relief=SUNKEN,
            cursor='pencil').pack(expand=True, fill=BOTH)
        Button(self, text='Source', command=self.browseSource).pack(expand=True)

    def start(self):
        self.hellos = 0
        self.pack(expand=True, fill=BOTH)
        self.master.title('Big Gui Demo')
        self.master.iconname('Big Gui')
        spawnme = lambda: self.spawn((sys.executable, __file__))

        self.menubar = [
            ('File', 0, 
                (
                     ('New...', 0, spawnme),
                     ('Open..', 0, self.selectOpenFile),
                     ('Quit..', 0, self.quit)
                )),
            ('Edit', 0,
                (
                    ('Cut', -1, self.notimplemented),
                     ('Paste', -1, self.notimplemented),
                     'separator',
                     ('Stuff', -1,
                        (
                            ('Clone', -1, self.clone),
                            ('More', -1, self.more)
                        )),
                     ('Delete', 0, lambda: 0),
                     [5],
                )),

            ('Play', 0,
                (
                    ('Hello', 0, self.greeting),
                    ('Popup', 0, self.dialog),
                    ('Demos', -1,
                        (
                            ('Optionmenus', 0, 
                                lambda: self.spawn((sys.executable,
                                '../Tour2/optionmenu.py'))),
                            ('Canvas', 0,
                                lambda: self.spawn((sys.executable,
                                    '../Tour2/canvasDraw_threaded_sleep.py'))),
                            ('Alarm', 0,
                                lambda: self.spawn((sys.executable,
                                    '../Tour2/alarm-withdraw.py'))),
                            ('Images', 0,
                                lambda: self.spawn((sys.executable,
                                    '../Tour2/viewer_thumbs_scrolled.py'))),
                            ('Others', 0,
                                lambda: self.spawn((sys.executable,
                                    '../Tour2/grid5b.py'))),
                            ('Pick Yourself', 0, self.pickDemo),
                        )),
            )),
        ]
        
        self.toolbar = [
                ('Quit', self.quit, dict(side=RIGHT)),
                ('Greet', self.greeting, dict(side=LEFT)),
                ('Popup', self.dialog, dict(side=LEFT, expand=True)),
            ]

if __name__ == '__main__':
    ClientTest().mainloop()

