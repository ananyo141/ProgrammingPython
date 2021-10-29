import sys, os
from socket_preview import client, server
from threading import Thread

if len(sys.argv) > 1:
    mode = int(sys.argv[1])
    if mode == 1:
        server()
    elif mode == 2:
        client("Child %s" % os.getpid())
else:
    for i in range(5):
        Thread(target=client, args=("Child %d" % i,)).start()

