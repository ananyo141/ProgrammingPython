# Use threading to delegate blocking calls to spawned threads
# and use callbacks to run blocks of code in the main thread

import threading, queue
from types import FunctionType

class ThreadRun:
    def __init__(self):
        self.__queue = queue.Queue()       # for internal usage

    def execute(self, nCalls: int = 5):
        """
        Execute the callbacks on the queue; default max per run = 5
        RUN IN MAIN THREAD ONLY
        """
        for i in range(nCalls):
            try:
                callback, args = self.__queue.get(block=False)
            except queue.Empty:
                break
            else:
                callback(*args)

    def _threadRun(self,
                   callback: FunctionType, # action to call in thread
                   args   : tuple,         # arbitrary tuple args to call with callback
                   context: tuple,         # tuple of args for `on*`handlers, for information
                   *,                      # only take keyword arguments after this
                   onExit: FunctionType,
                   onFail: FunctionType, 
                   onProgress: FunctionType = None):
        """
        Target for threading
        Run the given callback with args in a spawned thread
        Use function blocks `on*` FunctionTypes to register context
        with callables in queue to be run by main thread.
        """
        try:
            if onProgress is None:
                callback(*args)
            else:
                # callback will feed this function 'progress' arg(s) that will export 
                # a progress callable to the main thread queue from here; when called
                # uses that calling argument coupled with this scope context to enqueue
                # a callable to queue
                def progress(*progarg):
                    self.__queue.put((onProgress, progarg + context))
                callback(progress=progress, *args)

        except Exception as exc:
            self.__queue.put((onFail, (exc,) + context))
        else:
            self.__queue.put((onExit, context))

    def __call__(self, *args, daemon: bool = True, **kw):
        """
        Use as a functor that spawns threads
        Interface for calling the threaded `_threadRun` function
        """
        thread = threading.Thread(target=self._threadRun, 
                                  args=args, kwargs=kw)
        thread.daemon = daemon
        thread.start()

if __name__ == '__main__':
    import time
    from tkinter.scrolledtext import ScrolledText

    # Self test logic
    class _SelfTest(ScrolledText):
        SLEEP_TIME = 2
        NUM_THREAD = 10
        SPOOL_TIME = 100

        class _OddException(Exception):
            """
            Dummy exception to raise to test 
            catch exception in thread
            """

        def __init__(self, master=None):
            ScrolledText.__init__(self, master)
            self.pack(expand=True, fill='both')

            self.threadCounter = 0

            self.runner = ThreadRun()
            self.onEvent()
            # Click to trigger more threads
            self.bind('<Button-1>', self.onEvent)
            self.spoolQueue()

        def spoolQueue(self):
            """
            Spool the queue filled by worker threads
            for possible callbacks produced
            """
            self.runner.execute()
            self.after(self.SPOOL_TIME, self.spoolQueue)

        def onEvent(self, event = None):
            """
            Start a long running work on a thread with
            appropriate callback functions
            """
            for i in range(self.NUM_THREAD):
                self.threadCounter += 1
                name = f'Thread: {self.threadCounter}'

                self.runner(
                        self.threadaction,
                        (i,),
                        (name,),
                        onExit = self.exitHandler,
                        onFail = self.failHandler,
                        onProgress = self.progHandler,
                )

        def threadaction(self, thid: int, 
                         progress: FunctionType = None, count: int = 10):
            """
            Simulate long running thread operations that need to be
            decoupled for non-blocking gui
            """
            for i in range(count):
                if progress: progress(i)  # send progress updates
                time.sleep(self.SLEEP_TIME)
            if thid & 1: 
                raise self._OddException(f"Thread ID {thid} is odd")

        def _printText(self, msg: str):
            """
            Print the given message into scrolledtext (self)
            """
            self.insert('end', msg + '\n')
            self.see('end')

        def progHandler(self, thid, name):
            """
            Progress call in thread refers to progress call here,
            updates happen in main thread
            """
            self._printText(f'{name} Generated -> {thid}')

        def exitHandler(self, name):
            self._printText(f'{name} Exited')

        def failHandler(self, exceptionSpec, name):
            self._printText(f'{name} raised exception {str(exceptionSpec)}')
    

    # Call self test
    _SelfTest().mainloop()

