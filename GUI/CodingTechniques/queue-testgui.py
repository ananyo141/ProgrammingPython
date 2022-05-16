from tkinter import *
import time, queue, _thread
from tkinter.scrolledtext import ScrolledText

class Consumer(ScrolledText):
    NUM_THREAD = 5          # number of threads per callback
    COUNT_PER_THREAD = 15   # number of msg each producer counts upto
    MAX_PER_FETCH = 5       # number of msg each fetch in consumer gets

    def __init__(self, *args, **kw):
        ScrolledText.__init__(self, *args, **kw)
        self.queue = queue.Queue()
        self.bind('<Button-1>', self.makeThreads)
        self.consume()

    def makeThreads(self, event):
        for i in range(self.NUM_THREAD):
            _thread.start_new_thread(self.producer, (i,))

    def consume(self):
        for i in range(self.MAX_PER_FETCH):
            try:
                message = self.queue.get(block=False)
                self.insert(END, message + '\n')
                self.see(END)
            except queue.Empty:
                break
        self.after(250, self.consume)

    def producer(self, id: int):
        """
        Create number of producer threads that put values
        on queue
        """
        for i in range(self.COUNT_PER_THREAD):
            self.queue.put(f'Thread {id} -> Generated {i}')
            time.sleep(2)

if __name__ == '__main__':
    root = Tk()
    Consumer(root).pack(expand=True, fill=BOTH)
    mainloop()

