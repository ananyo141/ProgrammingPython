import os, time

def child(pipeout):
    zzz = 0
    while True:
        zzz = (zzz + 1) % 5
        time.sleep(zzz)
        msg = 'Child %d sending: %d' % (os.getpid(), zzz)
        os.write(pipeout, msg.encode())


def parent():
    pipein, pipeout = os.pipe()
    if os.fork() == 0:
        child(pipeout)
    else:
        pipeInObj = os.fdopen(pipein, 'r', 1)
        while True:
            print("Parent got : %s" % pipeInObj.readline())

if __name__ == '__main__': parent()
