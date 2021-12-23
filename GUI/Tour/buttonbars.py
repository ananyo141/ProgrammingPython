from tkinter import *

class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=TOP, anchor=W, **kw):
        Frame.__init__(self, parent, **kw)
        self.vars = []
        for pick in picks:
            var = IntVar()
            Checkbutton(self, text=pick,
                        variable=var,
            ).pack(side=side, anchor=anchor)
            self.vars.append(var)

    def report(self):
        return [x.get() for x in self.vars]

class Radiobar(Frame):
    def __init__(self, parent=None, picks=[], side=TOP, anchor=W, **kw):
        Frame.__init__(self, parent, **kw)
        self.var = StringVar(value=' ')
        for pick in picks:
            Radiobutton(self, text=pick,
                        variable=self.var,
                        value=pick,
            ).pack(side=side, anchor=anchor)

    def report(self):
        return self.var.get()

if __name__ == '__main__':
    from quitter import Quitter
    

    root = Tk()
    (osWidget := Radiobar(root, ['win', 'x11', 'mac'],
                          bd=2, relief=GROOVE,
    )).pack(side=LEFT, expand=True)

    (langWidget := Checkbar(root, ['Python', 'C#', 'Java', 'C++'],
                            bd=2, relief=RIDGE,
                            side=LEFT)).pack()

    (buttonFrame := Frame(bd=2, relief=SUNKEN)).pack(
                              expand=True, fill=BOTH)
    (allWidget := Checkbar(buttonFrame, ['All'])).pack(
                              side=LEFT)

    def peek(): 
        global osWidget, langWidget, allWidget
        print(osWidget.report(), langWidget.report(), allWidget.report())
        
    Quitter(buttonFrame).pack(side=RIGHT)
    Button(buttonFrame, text='Peek', 
           command=peek).pack(side=RIGHT)
    
    root.mainloop()
    
