import os, time, threading

def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = "Child sent %d\n" % zzz
        os.write(pipeout, msg.encode())
        zzz = (zzz + 1) % 5

def parent(pipein):
    file = os.fdopen(pipein)
    while True:
        data = file.readline()[:-1]
        #data = os.read(pipein, 32)     # data may look like overlapping with os.read(),
        print("Parent got [%s]" % data) # this is because child sends two msgs together as it hits time.sleep(0)

pipein, pipeout = os.pipe()
threading.Thread(target=child, args=(pipeout,)).start()
parent(pipein)

