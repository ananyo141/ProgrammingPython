import _thread, time

def counter(myId, count):
    for i in range(count):
        time.sleep(1)
        with mutex:
            print('[%s] => %d' % (myId, count))

for i in range(5):          # deploy 5 threads
    _thread.start_new_thread(counter, (i, 5))

mutex = _thread.allocate_lock()
time.sleep(6)
print("Main thread exiting")

