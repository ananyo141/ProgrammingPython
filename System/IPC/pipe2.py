import os, time

def child(pipeout):
    zzz = 0
    while True:
        zzz = (zzz + 1) % 5
        time.sleep(zzz)
        msg = "Child sent: %s\n" % zzz
        os.write(pipeout, msg.encode())

def parent():
    pipein, pipeout = os.pipe()
    if os.fork() == 0:
        os.close(pipein)    # close unused fd in child process
        child(pipeout)
    else:
        os.close(pipeout)   # close the unused fd in parent process
        pipeinFile = os.fdopen(pipein)
        while True:
            data = pipeinFile.readline()[:-1]
            print("Parent got %s" % data)

parent()
