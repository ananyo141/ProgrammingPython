import os, time, queue # for the exception class
from multiprocessing import Process, Queue

# expand on the Process class
class Counter(Process):
    label = ' @'
    def __init__(self, start, queue):
        self.state = start
        self.post  = queue       # queue object
        Process.__init__(self)

    # loop 3 times, each time incrementing self.state by
    # 1, and post results in queue object
    def run(self):
        for i in range(3):
            time.sleep(1)
            self.state += 1
            print(self.label, self.pid, self.state)
            self.post.put([self.pid, self.state])
        print(self.label, self.pid, '-')    # print results after looping
        
if __name__ == '__main__':
    print('Start', os.getpid())
    expected = 9

    post = Queue()
    p = Counter(0, post)
    q = Counter(100, post)
    r = Counter(1000, post)
    p.start(); q.start(); r.start()

    while expected:
        time.sleep(0.5)
        try:
            data = post.get(block=False)
        except queue.Empty:     # use the exception class from the queue module
            print("no data...")
        else:
            print('posted:', data)
            expected -= 1

    p.join(); q.join(); r.join()
    print("finish", os.getpid(), r.exitcode)

