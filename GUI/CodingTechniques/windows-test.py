from tkinter import mainloop, Button
from windows import MainWindow, PopupWindow, ComponentWindow

def _win_test():
    # mixin to hold dummy buttons
    class content:
        def __init__(self):
            Button(self, text='Larch', command=self.quit).pack()
            Button(self, text='Sing', command=self.destroy).pack()
    
    class ContentMix(MainWindow, content):
        def __init__(self, *args, **kw):
            MainWindow.__init__(self, *args, **kw)
            content.__init__(self)
    ContentMix('MainMix')

    class ContentMix(PopupWindow, content):
        def __init__(self, *args, **kw):
            PopupWindow.__init__(self, *args, **kw)
            content.__init__(self)
    prev = ContentMix('PopMix')

    class ContentMix(ComponentWindow, content):
        def __init__(self, *args, **kw):
            ComponentWindow.__init__(self, *args, **kw)
            content.__init__(self)
    ContentMix(prev)

    # subclass usage
    class SubPopup(PopupWindow):
        def __init__(self):
            PopupWindow.__init__(self, 'Popup', 'SubClass')
            Button(self, text='Pine', command=self.quit).pack()
            Button(self, text='Larch', command=self.destroy).pack()
    SubPopup()

    # non-class usage, as a parent widget
    win = PopupWindow('Popup', 'NonClass')
    Button(win, text='Pine', command=win.quit).pack()
    Button(win, text='Larch', command=win.destroy).pack()

    mainloop()

if __name__ == '__main__':
    _win_test()

