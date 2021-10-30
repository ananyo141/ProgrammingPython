import time
from multiprocessing import Process, Pipe

def child(pipe):
    time.sleep(5)
    pipe.send("Done")
    pipe.close()

if __name__ == '__main__':
    parentEnd, childEnd = Pipe()
    Process(target=child, args=(childEnd,)).start()
    if parentEnd.recv(): print("Got it")    # blocks the caller until it gets message
                                            # from the child
