
from socket import *

PORT = 50008
HOST = 'localhost'
def redirectOut(port=PORT, host=HOST):
    " Create a socket object and return the file interface "
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    return sock.makefile('w')

def redirectIn(port=PORT, host=HOST): ...
def redirectBothAsClient(port=PORT, host=HOST): ...
def redirectBothAsServer(port=PORT, host=HOST): ...

