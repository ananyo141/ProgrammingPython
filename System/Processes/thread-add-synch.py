import threading, time

count = 0

def adder(addLock):
    global count
    with addLock:
        count += 1
    time.sleep(0.5)
    with addLock:
        count += 1

threads = []
addLock = threading.Lock()
for i in range(100):
    thread = threading.Thread(target = adder, args = (addLock,))
    threads.append(thread)
    thread.start()

for thread in threads: thread.join()
print(count)

