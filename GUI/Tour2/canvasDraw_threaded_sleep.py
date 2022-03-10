" Use time sleep calls in threads to handle multiple move requests "
import _thread
from tkinter import *
from canvasDraw_manual_timesleep import CanvasSleep

class CanvasThread(CanvasSleep):
    def onTagRotate(self, tag, numRotate=5):
        _thread.start_new_thread(CanvasSleep.onTagRotate, 
                    (self, tag, numRotate))

if __name__ == '__main__':
    CanvasThread()
    mainloop()

