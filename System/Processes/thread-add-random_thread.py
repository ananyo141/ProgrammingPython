import _thread, time

exitMutexes = [_thread.allocate_lock() for i in range(100)]
count = 0
def adder(thId):
    global count
    count += 1
    time.sleep(0.5)
    count += 1
    exitMutexes[thId].acquire()

for i in range(100):
    _thread.start_new_thread(adder, (i,))

while not all([mutex.locked() for mutex in exitMutexes]): pass
print(count)
