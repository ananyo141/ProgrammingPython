from tkinter import *

# all the bind event handlers
def printEventPos(event):
    print(f"Widget: %s  X: %s, Y : %s" % (event.widget, event.x, event.y))

def showAllDetails(event):
    print(event)
    for attr in dir(event):
        if attr.startswith('__'): continue
        print(attr, '=>', getattr(event, attr))

def onLeftClick(event):
    print("Got left click")
    printEventPos(event)

def onRightClick(event):
    print("Got right click")
    printEventPos(event)

def onMiddleClick(event):
    print("Got middle click")
    printEventPos(event)
    showAllDetails(event)

def onDoubleClick(event):
    print("Got double clicked")
    event.widget.master.quit()

def onLeftDrag(event):
    print("Got dragged")
    printEventPos(event)

def onKeyPress(event):
    print(f"Pressed {event.char} key!")

def onUpArrow(event):
    print("Pressed up")

def onEnterKey(event):
    print("Pressed return")

# root gui
root = Tk()
root.title('Clickity Pipity')
widget = Label(root, text="Label with event handlers")
widget.config(font=('courier', 15, 'underline italic'))
widget.config(bg='red', fg='blue', height=10, width=30)
widget.pack(expand=True, fill=BOTH)

# install handlers
widget.bind('<Button-1>',  onLeftClick)
widget.bind('<Button-3>',  onRightClick)
widget.bind('<Button-2>',  onMiddleClick)
widget.bind('<B1-Motion>', onLeftDrag)
widget.bind('<Double-1>',  onDoubleClick)
widget.bind('<KeyPress>',  onKeyPress)
widget.bind('<Up>',        onUpArrow)
widget.bind('<Return>',    onEnterKey)

widget.focus()
root.mainloop()

