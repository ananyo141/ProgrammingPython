# Use the guimaker generic template to create gradually specific
# subclass hierarchy

from tkinter import *
from tkinter.ttk import *
from guimixin import GuiMixin        # mixin class
from guimaker import GuiNativeMaker  # create specialized subclass
from guimaker import gmakerlog

# Build on the guimaker to create specific menus and toolbars
# for derived classes
class ShellGui(GuiMixin, GuiNativeMaker):
    def start(self):
        self.createMenuStruct()    # logic to add menu datastructure
        self.createToolStruct()    # same, for toolbar
        self.pack(expand=True, fill=BOTH)
        self.master.title('Shell Gui')
        self.master.iconname('Shell Gui')

    def makeWidgets(self):
        def handleListClick(event):
            selection = lbox.get(ACTIVE)
            self.runCommand(selection)

        lboxFrame = Frame(self)
        lboxFrame.pack(expand=True, fill=BOTH)

        lbox = Listbox(lboxFrame, width=30, height=5)
        scroll = Scrollbar(lboxFrame, command=lbox.yview)
        lbox.config(yscrollcommand=scroll.set)

        scroll.pack(side=RIGHT, fill=Y)
        lbox.pack(expand=True, fill=BOTH)
        lbox.bind('<Double-1>', handleListClick)

        for label, command in self.fetchCommands():
            lbox.insert(END, label)

    def createMenuStruct(self):
        toolEntries = [ (label, -1, action) for label, action in
                        self.fetchCommands() ]
        gmakerlog.debug(f"{toolEntries = }")
        self.menubar = [
                ('File', 0, 
                    (('New', 0, self.clone),
                    ('Quit', -1, self.quit) )),
                ('Tools', 0, tuple(toolEntries)),
            ]

    def createToolStruct(self):
        self.toolbar = [(label, action, dict(side=LEFT)) for label, action in self.fetchCommands() 
                        if self.forToolbar(label)]
        self.toolbar.append(('Quit', self.quit, dict(side=RIGHT)))

    def forToolbar(self, label):
        """ 
        Predicate function to check if the given label
        should be included in the toolbar 
        """
        return True # default all

    def runCommand(self, label):
        " Run command according to the given label selected from listbox "
        raise NotImplementedError

    def fetchCommands(self):
        " Subclass to return list like instances of (label, action) "
        raise NotImplementedError

# List and Dict adapters of ShellGui class
class ListShellGui(ShellGui):
    def fetchCommands(self):
        return self.myMenu         # already a list or tuple

    def runCommand(self, label):
        # use linear search in case of a list
        # to search for callback and invoke
        for key, action in self.myMenu:
            if key == label:
                action()

class DictShellGui(ShellGui):
    def fetchCommands(self):
        return self.myMenu.items() # a dict of labels and callbacks
    
    def runCommand(self, label):
        self.myMenu[label]()       # use dict notation to invoke callback

