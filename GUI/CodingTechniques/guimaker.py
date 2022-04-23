from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgb
import logging, os
logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(lineno)d - %(levelname)s - %(message)s',
        datefmt='%d/%m/%Y %I:%M:%S %p',
        filename=os.path.splitext(os.path.basename(__file__))[0] + '.log',
        filemode='w',
    )
gmakerlog = logging.getLogger(__file__)
logging.disable(logging.CRITICAL)

# Create a base class for gui formation
class GuiMaker(Frame):
    # keep menu and toolbar structures in class attrs,
    # and give option to change in self.start
    menubar = []
    toolbar = []

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.start()
        self.makeMenubar()
        self.makeToolbar()
        self.makeWidgets()

    def start(self):
        " Reserved for using menu/toolbar structures containing `self` "

    # create a menu help button
    def help(self):
        " Change in subclass "
        msgb.showerror("Not Implemented", "Sorry help not defined")

    # keep space for an optional widgets area, 
    # where it can be subclassed
    def makeWidgets(self):
        Label(self, width=40, relief=GROOVE,
              text=f"Widgets Go Here, using {self.__class__.__name__}",
              cursor='crosshair',
        ).pack(expand=True, fill=BOTH)

    def makeToolbar(self):
        """
        toolbar structure contains an iterable of 
        (label, command and packcfg) where,
        label   -> str
        command -> function or lambda or boundmethod
        packcfg -> dictionary of tkinter pack configs
        """
        gmakerlog.debug(f'{self.toolbar = }', exc_info=True)
        if self.toolbar:
            toolbar = Frame(self, cursor='gumby', relief=FLAT)
            toolbar.pack(side=BOTTOM, fill=X)
            for (label, command, packcfg) in self.toolbar:
                Button(toolbar, text=label, command=command).pack(**packcfg)

    def makeMenubar(self):
        gmakerlog.debug(f'{self.menubar = }')
        menuFrame = Frame(self)
        menuFrame.pack(fill=X)
        for (label, key, items) in self.menubar:
            menubtn  = Menubutton(menuFrame, text=label, underline=key)
            pulldown = Menu(menubtn, tearoff=False)
            menubtn.pack(side=LEFT)
            menubtn.config(menu=pulldown)
            self.makeMenuItems(pulldown, items)

    """
    create menubar and parse menubar structure to create
        - Separators
        - Disabled list items
        - Normal command handlers
        - Nested cascading menus
    """
    @classmethod
    def makeMenuItems(cls, pulldown, items):
        # traverse the items list
        for item in items:
            # if item is a string literal
            if item == 'separator':
                pulldown.add_separator()
            # if item is a list-only, then use the numbers 
            # in list to disable items in the menu
            elif isinstance(item, list):
                for num in item:
                    pulldown.entryconfig(num, state=DISABLED)
            # if item is tuple, and third value is not a
            # tuple itself, then add entry and register a callback
            elif not isinstance(item[2], tuple):
                pulldown.add_command(label=item[0], underline=item[1],
                                      command=item[2])
            # else if tuple and third value is a tuple,
            # add a submenu
            elif isinstance(item[2], tuple):
                submenu = Menu(pulldown, tearoff=False)
                cls.makeMenuItems(submenu, item[2])    # recurse to build sublist
                pulldown.add_cascade(label=item[0], underline=item[1],
                                     menu=submenu)
            else:
                raise ValueError(
                        "Items in list should either be string 'separator', "
                        "a list of disabled entry numbers, a tuple of label, underline "
                        "and command or a tuple with label, underline and "
                        "nested menu tuple")

# As guimaker is already frame based
GuiFrameMaker = GuiMaker

"""
Inherit the same methodology but change the menu
mechanism to support toplevel native-menubars
instead of embedding menubuttons in frames
"""
class GuiNativeMaker(GuiMaker):
    def makeMenubar(self):
        menuNative = Menu(self.master, tearoff=False)
        self.master.config(menu=menuNative)
        for (label, key, items) in self.menubar:
            pulldown = Menu(menuNative, tearoff=False)
            menuNative.add_cascade(label=label, underline=key, menu=pulldown)
            self.makeMenuItems(pulldown, items)

# Test the classes
def testMenuMakers():
    import sys
    from guimixin import GuiMixin

    testMenuBar = [('File', 0, (('New', 0, lambda: 0),) )]
    testToolbar = [
            ('Print', 0, {"side": LEFT, "padx": 3}),
            ('Quit', sys.exit, {"side": RIGHT, "padx": 5}),
        ]
    class TestGuiFrameMaker(GuiMixin, GuiFrameMaker):
        menubar = testMenuBar
        toolbar = testToolbar[:]        # make a copy to modify list

        def start(self):
            self.toolbar.append( ('Help', self.help, {}) ) # guimixin's help

    class TestGuiNativeMaker(GuiNativeMaker):
        menubar = testMenuBar
        toolbar = testToolbar.copy()    # same, to modify list

        def start(self):
            self.toolbar.append(('Help', self.help, {},) ) # guimaker's help

    root = Tk()
    win = Toplevel(root)
    TestGuiFrameMaker(root).pack(expand=True, fill=BOTH)
    TestGuiNativeMaker(win).pack(expand=True, fill=BOTH)
    mainloop()

if __name__ == '__main__':
    testMenuMakers()

