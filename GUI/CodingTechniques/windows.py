# Encapsulate the border logic - Icon, Title and Exits
# Provide widgets that work similar in terms of these
import os, glob
from tkinter import *
from tkinter.messagebox import askyesno, showerror

class _window:
    foundIcon  = None
    iconPattr  = '*.ico'
    iconModule = 'windows.ico'

    def borderConfig(self, app: str, kind: str = '', iconfile: str = '') -> None:
        """
        Set the corresponding title, iconname, iconpic and quit protocol
        of the widget
        """
        self.title(app if not kind else app + ' - ' + kind)
        self.iconname(app)
        iconname = iconfile if iconfile else self.findIcon()
        try:
            self.iconbitmap(iconname)
        except: pass
        self.protocol('WM_DELETE_WINDOW', self.quit)

    def findIcon(self):
        """
        Find a suitable icon from the current directory or
        script directory and return. Return foundIcon if already found
        """
        if _window.foundIcon: return _window.foundIcon
        currIcons = glob.glob(self.iconPattr)
        finalIconFile = None
        if currIcons:
            finalIconFile = currIcons[0]
        else:
            import importlib
            module = importlib.__import__(__name__)
            path = __name__.split('.')
            for mod in path[1:]:
                module = getattr(module, mod)
            dirname = os.path.dirname(module.__file__)
            iconpath = os.path.join(dirname, self.iconModule)
            if os.path.exists(iconpath): 
                finalIconFile = iconpath
        _window.foundIcon = finalIconFile
        return finalIconFile

    def okayToQuit(self):
        return True

    def quit(self):
        self.okayToQuit() and \
           askyesno('Confirmation', 'Are you sure you want to exit?') and \
           self.destroy()   # assume has destroy method available in widget


class MainWindow(Tk, _window):
    " Provide Customized Tk main window "
    def __init__(self, app, kind='', iconfile=''):
        Tk.__init__(self)
        self.__app = app
        self.borderConfig(app, kind, iconfile)

class PopupWindow(Toplevel, _window):
    " Provide Customized pop up window "
    def __init__(self, app, kind='', iconfile=''):
        Toplevel.__init__(self)
        self.__app = app
        self.borderConfig(app, kind, iconfile)

class QuietPopupWindow(PopupWindow):
    def quit(self):
        self.destroy()

class ComponentWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(expand=True, fill=BOTH)
        self.config(relief=RIDGE, bd=2)

    def quit(self):
        showerror('Invalid', 'Not supported in attach mode')

