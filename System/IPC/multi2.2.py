import os, random
from multiprocessing import Process, Pipe

def child(ident, pipe):
    if random.randint(0, 4) == 3:
        pipe.send("Child(id: %d) %d got %d" % (ident, os.getpid(), 3))
        pipe.close()

if __name__ == '__main__':
    parentEnd, childEnd = Pipe()
    for i in range(20):
        Process(target=child, args=(i, childEnd)).start()
    data = parentEnd.recv()
    print("Parent got [%s]" % data)
    print("Main process exiting")

