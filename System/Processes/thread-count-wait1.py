import _thread

NUM_THREADS = 10
NUM_RANGE = 100
stdoutMutex = _thread.allocate_lock()
exitMutexes = [_thread.allocate_lock() for i in range(NUM_THREADS)] # create exit mutex for each thread to 
                                                                    # signal main thread of exit
# target function
def counter(myId, count):
    for i in range(count):
        with stdoutMutex:
            print(f"[{myId}] => {i}")
    exitMutexes[myId].acquire()       # signal to main thread

# spawn threads and make them use function
for thID in range(NUM_THREADS):
    _thread.start_new_thread(counter, (thID, NUM_RANGE))

while not all([mutex.locked() for mutex in exitMutexes]): pass # a busy loop that incessantly checks  
                                                               # if the threads are done
print("Main thread exiting")

