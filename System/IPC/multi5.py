import os
from multiprocessing import Process

def runprogram(arg):
    os.execlp('python', 'python', 'child.py', str(arg))

if __name__ == '__main__':
    # create 5 processes and run program and exit main process
    for i in range(5):
        Process(target=runprogram, args=(i,)).start() # each process now runs a separate program
    print("Parent exit")

