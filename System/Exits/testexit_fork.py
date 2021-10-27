import os
exitstatus = 0

def child():
    global exitstatus
    exitstatus += 1
    print("Child", os.getpid(), "Exiting")
    os._exit(exitstatus)
    print("Never reached")

def parent():
    while True:
        if os.fork() == 0: child()
        else: 
            pid, status = os.wait()
            print("Parent got", pid, status, status >> 8)
            if input() == 'q': break

if __name__ == '__main__': parent()

