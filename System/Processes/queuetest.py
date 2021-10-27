import _thread, queue, time

NUM_CONSUMERS = 2
NUM_MESSAGES = 4
NUM_PRODUCERS = 4

TIME_CONS = 0.25
TIME_PROD = 0.5

def producer(thID, dataqueue, num_messages):
    for msg_num in range(num_messages):
        time.sleep(TIME_PROD)
        dataqueue.put(f"prod id: {thID} -> {msg_num}")

# create a perpetual running loop that checks for feed from producers
def consumer(dataqueue, printLock):
    while True:
        time.sleep(TIME_CONS)
        try:
            dataGot = dataqueue.get(block = False)
        except queue.Empty: pass
        else: 
            with printLock:
                print(f"Got Data: [{dataGot}]")

if __name__ == '__main__':
    dataQueue = queue.Queue()   # queue object to sync data between threads
    printLock = _thread.allocate_lock()
    # create producer threads
    for prodTh in range(NUM_PRODUCERS):
        _thread.start_new_thread(producer, (prodTh, dataQueue, NUM_MESSAGES))
    # create consumer threads
    for consumerTh in range(NUM_CONSUMERS):
        _thread.start_new_thread(consumer, (dataQueue, printLock))

    time.sleep((NUM_CONSUMERS * TIME_CONS) + (NUM_PRODUCERS * TIME_PROD))
    print("Main thread exiting")
