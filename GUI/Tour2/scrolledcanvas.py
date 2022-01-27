# Implement a scrolled canvas
import tkinter as tk

class ScrolledCanvas(tk.Frame):
    def __init__(self, parent=None, color='red'):
        tk.Frame.__init__(self, parent)
        self.pack(expand=True, fill='both')
        canv = tk.Canvas(self, width=300, height=400, bg=color)
        canv.config(scrollregion=(0, 0, 300, 1700), highlightthickness=0)
        
        scroll = tk.Scrollbar(self, command=canv.yview)
        canv.config(yscrollcommand=scroll.set)
        scroll.pack(side='right', fill='y')
        canv.pack(expand=True, fill='both')
        self.canv = canv
        self.fillcanvas()
        canv.bind('<Double-1>', self.onDoubleClick)

    def fillcanvas(self):
        scrollregy = 1700 - 50
        numtext = 30
        inc = scrollregy / numtext
        for i in range(0, numtext):
            self.canv.create_text(50, inc*i + 50, text=f'Spam {i+1}', 
                                  fill='white')

    def onDoubleClick(self, event):
        print(event.x, event.y) # display coord
        print(self.canv.canvasx(event.x), self.canv.canvasy(event.y)) # canvas coord

if __name__ == '__main__': ScrolledCanvas().mainloop()

