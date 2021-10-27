import _thread

exitstat = 0

def child():
    global exitstat
    exitstat += 1
    threadid = _thread.get_ident() # may be reused after thread exits
    print("Hello from thread: ", threadid, exitstat)
    _thread.exit()
    print("Never reached")

def parent():
    while True:
        _thread.start_new_thread(child, ())
        if input() == 'q': break

if __name__ == '__main__': parent()

