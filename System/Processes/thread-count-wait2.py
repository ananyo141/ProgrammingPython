import _thread

NUM_THREADS = 10
NUM_RANGE = 100

stdoutMutex = _thread.allocate_lock()
threadStatuses = [False] * NUM_THREADS      # global list that manages thread statuses

def counter(thID, count):
    for i in range(count):
        with stdoutMutex:
            print(f"[{thID}] => {i}")
    threadStatuses[thID] = True

for i in range(NUM_THREADS):
    _thread.start_new_thread(counter, (i, NUM_RANGE))

while not all(threadStatuses): pass
print("Main thread exiting")

