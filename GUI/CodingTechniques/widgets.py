# A `function`-al approach to gui code reuse
# -- Create, pack, configure widgets and return them

from tkinter import *
from tkinter.ttk import *

def createWidget(master=None, widgetType=Label, 
                 side=TOP, expand=True, fill=BOTH, 
                 **configs):
    " Get a prebuilt tkinter widget "
    widget = widgetType(master, **configs)
    widget.pack(side=side, expand=expand, fill=fill)
    return widget

if __name__ == '__main__':
    root = Tk()
    createWidget(root, Button)
    createWidget(root, Entry)
    createWidget(root, Label, text='Hi')
    mainloop()

