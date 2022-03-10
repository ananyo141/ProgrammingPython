" Use widget after handlers to schedule canvas move "

from tkinter import *
from canvasDraw_manual_timesleep import CanvasSleep

class CanvasAfter(CanvasSleep):
    def moveAfter(self, allmoves, tag):
        (diffx, diffy), allmoves = allmoves[0], allmoves[1:]
        self.canv.move(tag, diffx, diffy)
        if allmoves:
            self.canv.after(250, self.moveAfter, allmoves, tag)

    def onTagRotate(self, tag):
        allmoves = self.rotateOffsets * 5  # use manual move offsets instead of loop
        self.moveAfter(allmoves, tag)

if __name__ == '__main__':
    CanvasAfter()
    mainloop()

