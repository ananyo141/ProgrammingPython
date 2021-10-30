import os
from multiprocessing import Process, Lock

def whoami(label, lock):
    msg = "label: %s, name: %s, pid: %d"
    with lock:
        print(msg % (label, __name__, os.getpid()))

if __name__ == '__main__':
    lock = Lock()   # create the lock object to sync output to stdout
    process = Process(target=whoami, args=('Child process', lock)) # spawn a single child
    process.start() # start and,
    process.join()  # wait for finish

    # spawn 5 processes, and exit 
    for i in range(5):
        Process(target=whoami, args=('Child %d' % (i + 1), lock)).start()
    with lock:
        print("Main process(pid: %d) exiting" % os.getpid())

