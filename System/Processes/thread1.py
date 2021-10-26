import _thread, time

def child(tid):
    with mutex:
        print("Hello from thread: %d" % tid)

def parent():
    thread = 0
    while True:
        thread += 1
        _thread.start_new_thread(child, (thread,))    # call: _thread.start_new_thread(child, (thread,)) 
        if thread == 500: break                       # lambda possible in threads, not processes

if __name__ == '__main__':
    mutex = _thread.allocate_lock()
    parent()
    time.sleep(3)

