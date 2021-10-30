import os
from multiprocessing import Process, Pipe

def child(pipe):
    '''
    send something in the pipe object
    '''
    msg = "Sending over pipe from pid: %d" % os.getpid()
    pipe.send(msg)
    pipe.close()

def talker(pipe):
    '''
    send something over pipe and recieve message from parent
    '''
    pipe.send("Shiba Inu is my favourite dog uwu")
    reply = pipe.recv()
    print("Talker(pid: %d) got [%s] from parent %d" % 
                            (os.getpid(), reply, os.getppid()))
    pipe.close()

if __name__ == '__main__':
    # create a child process and listen to pipe
    parentEnd, childEnd = Pipe()
    Process(target=child, args=(childEnd,)).start() # start off process
    replyFromChild = parentEnd.recv()
    parentEnd.close()       # close pipe
    print("Got [%s] from child" % replyFromChild)

    # create a talker that sends and recieves from pipe
    parentEnd, childEnd = Pipe()
    talkerChild = Process(target=talker, args=(childEnd,))
    talkerChild.start()

    # receive from talker
    print("Parent got from talker: [%s]" % parentEnd.recv())
    # send to talker
    parentEnd.send({x*2 for x in "spam"})
    talkerChild.join()
    parentEnd.close()
    print("Parent exiting")

