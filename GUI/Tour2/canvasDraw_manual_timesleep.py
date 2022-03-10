"""
Use Manual time sleep and update calls to use animation
"""

import time
from tkinter import *
from canvasDraw import CanvasEvent as CanvEv

class CanvasSleep(CanvEv):
    rotateOffsets = ((+20,0), (0,+20), (-20,0), (0,-20))

    def __init__(self, *args, **kw):
        CanvEv.__init__(self, *args, **kw)
        self.canv.create_text(100, 50, text='Press O to rotate ovals and R to'
                                            ' rotate rectangles')
        self.shapes = [self.canv_create_oval_tagged,
                       self.canv_create_rectangle_tagged]

    def bindEvents(self):
        CanvEv.bindEvents(self)
        self.canv.master.bind('<KeyPress-o>', 
                lambda event: self.onTagRotate('oval'))
        self.canv.master.bind('<KeyPress-r>', 
                lambda event: self.onTagRotate('rectangle'))

    def canv_create_oval_tagged(self, x1, y1, x2, y2):
        objectId = self.canv.create_oval(x1, y1, x2, y2, fill='red')
        self.canv.itemconfig(objectId, tag='oval')
        return objectId

    def canv_create_rectangle_tagged(self, x1, y1, x2, y2):
        objectId = self.canv.create_rectangle(x1, y1, x2, y2, fill='blue')
        self.canv.itemconfig(objectId, tag='rectangle')
        return objectId

    def onTagRotate(self, tag, numRotate=5):
        for i in range(numRotate):
            for diffx, diffy in self.rotateOffsets:
                self.canv.move(tag, diffx, diffy)
                self.canv.update()
                time.sleep(0.25)

if __name__ == '__main__':
    CanvasSleep()
    mainloop()

