import os, _thread
from queue import Queue, Empty
from tkinter.scrolledtext import ScrolledText

class RedirectedStream:
    TERM_TOKEN = '<end>'
    SPOOL_TIME = 1000

    class _GuiOutput(ScrolledText):
        def __init__(self, master=None):
            ScrolledText.__init__(self, master)
            self.pack(expand=True, fill='both')

        def write(self, line):
            self.insert('end', line)
            self.see('end')

    class _CommandData:
        def __init__(self, *, output, input, queue):
            self.output = output
            self.input  = input
            self.queue  = queue


    def __init__(self, master=None):
        self.root = master

    def producer(self, dat):
        while True:
            line = dat.input.readline()
            if not line:
                dat.queue.put(self.TERM_TOKEN)
                break
            dat.queue.put(line)

    def consumer(self, dat):
        try:
            line = dat.queue.get(block=False)
        except Empty:
            pass
        else:
            if line == self.TERM_TOKEN:
                return             # dont call after anymore
            dat.output.write(line)
        dat.output.after(self.SPOOL_TIME, lambda: self.consumer(dat))

    def __call__(self, command):
        " Open up a new widget to and execute the command "
        threadData = self._CommandData(
            output = self._GuiOutput(self.root),
            queue  = Queue(),
            input  = os.popen(command),
        )
        # spawn in a separate thread
        _thread.start_new_thread(self.producer, (threadData,))
        # gui runs in main
        self.consumer(threadData)

if __name__ == '__main__':
    import tkinter as tk
    # COMMAND = 'python3 -u socket-nongui.py'
    COMMAND = 'ls -l'

    root = tk.Tk()
    def spawn():
        popup = tk.Toplevel(root)
        runner = RedirectedStream(popup)
        runner(COMMAND)

    tk.Button(root, text='Go', command=spawn).pack()
    tk.Button(root, text='Quit', command=root.quit).pack()

    tk.mainloop()

