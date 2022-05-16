from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.simpledialog import askstring

class GuiOutput:
    font = ('Courier', 9, 'italic')
    def __init__(self, master=None):
        self.text = None
        if master: self.popup(master)

    def popup(self, master=None):
        if self.text: return
        self.text = ScrolledText(master or Toplevel())
        self.text.config(font = self.font)
        self.text.pack()

    def write(self, msg):
        self.popup()
        self.text.insert(END, msg)
        self.text.see(END)
        self.text.update()

    def writelines(self, lines):
        for line in lines: self.write(line)

class GuiInput:
    def __init__(self):
        self.buffer = ''

    @staticmethod
    def inputline():
        line = askstring('Input', 'Enter')
        return line + '\n' if line else ''

    def read(self, byte=None):
        if not self.buffer:
            self.buffer = self.inputline();
        if byte:
            text, self.buffer = self.buffer[:byte], self.buffer[byte:]
            return text
        text, self.buffer = self.buffer, ''
        while True:
            line = self.inputline()
            if not line: break   # read till eof
            text += line
        return text

    def readline(self):
        text = self.buffer if self.buffer else self.inputline()
        self.buffer = ''
        return text

    def readlines(self):
        text = self.read()
        return text.split('\n')

def redirectedGuiFunc(func, *args, **kw):
    import sys
    savestreams = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = GuiInput(), GuiOutput()
    funcReturn = func(*args, **kw)
    sys.stdin, sys.stdout = savestreams
    return funcReturn

def redirectedGuiShellCmd(command):
    import os
    output = GuiOutput()
    proc = os.popen(command, mode='r')
    while line := proc.readline():
        output.write(line)

if __name__ == '__main__':
    def makeUpper():
        while True:
            try:
                text = input("Enter message:")
            except: break
            print(text.upper())
        print("End of file")

    def makeLower(inp, out):
        text = inp.readline()
        out.write(text.lower())

    root = Tk()
    Button(root, text='Redirected Func', command=lambda:
            redirectedGuiFunc(makeUpper)).pack(fill=X)
    Button(root, text='Manual File Interfacing', command=lambda:
            makeLower(GuiInput(), GuiOutput())).pack(fill=X)
    Button(root, text='Redirected Shell', command=lambda:
            redirectedGuiShellCmd('ls -a')).pack(fill=X)
    mainloop()

