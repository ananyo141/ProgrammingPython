import os, sys, time
fifoname = '/tmp/fifo'

def child(fifoname):
    fifo = os.open(fifoname, os.O_WRONLY) # open as file descriptor
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = "Child (PID: %d): %d\n" % (os.getpid(), zzz)
        os.write(fifo, msg.encode())
        zzz = (zzz + 1) % 5

def parent(fifoname):
    fifo = open(fifoname, 'r')
    while True:
        line = fifo.readline()[:-1]  # discard newline, blocks caller
        print("Parent(%d) got [%s]" % (os.getpid(), line))

if __name__=='__main__':
    # make the fifo (named pipe) if not exists
    if not os.path.exists(fifoname):
        os.mkfifo(fifoname)
    if len(sys.argv) == 1:
        parent(fifoname)
    else:
        child(fifoname)

