import os, time

def child(pipeout):
    zzz = 0
    time.sleep(zzz)
    msg = "Child %d: %03d" % (os.getpid(), zzz)
    os.write(pipeout, msg.encode())
    zzz = (zzz + 1) % 5

def parent():
    pipein, pipeout = os.pipe()
    while True:
        if os.fork() == 0: child(pipeout)
        else: 
            while True:
                line = os.read(pipein, 32)
                print("Parent %d got [%s] at %s" % (os.getpid(), line, time.asctime()))

if __name__ == '__main__': parent()

