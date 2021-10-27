import threading, queue, time

def consumer(consumerID, dataqueue, printLock): 
    while True:
        try:
            data = dataqueue.get(block=False)
        except queue.Empty: pass
        else:
            with printLock:
                print(f"Consumer: {consumerID} got [{data}]")

def producer(producerID, dataqueue, num_messages, produce_time):
    for i in range(num_messages):
        time.sleep(produce_time)
        dataqueue.put(f"Producer: {producerID} => Message: {i}")

if __name__ == '__main__':
    NUM_CONSUMERS = 2
    NUM_MESSAGES = 4
    NUM_PRODUCERS = 4
    PRODUCER_TIME = 0.25

    dataQueue = queue.Queue()
    printLock = threading.Lock()
    
    for consumer_id in range(NUM_CONSUMERS):
        consumerThread = threading.Thread(target=consumer, args=(consumer_id, dataQueue, printLock))
        consumerThread.daemon = True
        consumerThread.start()

    waitfor = []
    for producer_id in range(NUM_PRODUCERS):
        producerThread = threading.Thread(target=producer, args=(producer_id, dataQueue, NUM_MESSAGES, PRODUCER_TIME))
        waitfor.append(producerThread)
        producerThread.start()

    for thread in waitfor: thread.join()
    print("Main thread exiting")

