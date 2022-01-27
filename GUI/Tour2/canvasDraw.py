import tkinter as tk

# Click creates new object
# Drag resizes object
# Right Click moves latest to cursor
# Left double click deletes all

class CanvasEvent:
    def __init__(self, parent=None, size=(300,300)):
        canv = tk.Canvas(parent, width=size[0], 
                         height=size[1], bg='beige')
        canv.pack(expand=True, fill='both')
        self.drawLast  = None
        self.shapes = [canv.create_oval, canv.create_rectangle]
        self.canv   = canv
        self.bindEvents()

    def bindEvents(self):
        self.canv.bind('<Button-1>',  self.onClick)
        self.canv.bind('<B1-Motion>', self.onDrag)
        self.canv.bind('<Double-1>',  self.onDoubleClick)
        self.canv.bind('<Button-3>',  self.onRightClick)

    def onClick(self, event):
        self.drawNew = self.shapes[0]       # select a shape
        self.shapes = self.shapes[1:] + self.shapes[:1] # shift shapes
        self.start = (event.x, event.y) # record starting coord
        self.drawLast = None

    def onDrag(self, event):
        if self.drawLast:
            self.canv.delete(self.drawLast)
        self.drawLast = self.drawNew(self.start[0], self.start[1], event.x, event.y)

    def onDoubleClick(self, event):
        self.canv.delete('all')

    def onRightClick(self, event):
        if self.drawLast:
            diffX, diffY = (event.x - self.start[0]), (event.y - self.start[1])
            self.canv.move(self.drawLast, diffX, diffY)
            self.start = event.x, event.y

if __name__ == '__main__': 
    CanvasEvent()
    tk.mainloop()

