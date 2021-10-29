from socket import socket, AF_INET, SOCK_STREAM

host = 'localhost'
port = 9330

def server():
    sock = socket(AF_INET, SOCK_STREAM)     # create a socket object
    sock.bind(('', port))                   # bind it to the port on system
    sock.listen(5)                          # listen for upcoming connections
    while True:
        conn, addr = sock.accept()          # blocks the caller, returns connection obj and addr
        data = conn.recv(1024)              # send and recieve data
        reply = "Server got [%s]" % data
        conn.send(reply.encode())

def client(name):
    # create a socket object
    sock = socket(AF_INET, SOCK_STREAM)
    # connect to the server port
    sock.connect((host, port))
    sock.send(f'Child{name}'.encode())
    data = sock.recv(1024)
    sock.close()
    print("Child got [%s]" % data)

if __name__ == '__main__':
    from threading import Thread
    # make a daemon server thread
    sThread = Thread(target=server)
    sThread.daemon = True
    sThread.start()
    # create 5 client threads
    for i in range(5):
        Thread(target=client, args=("Child %d" % i,)).start()

