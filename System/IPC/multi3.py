import os
from multiprocessing import Process, Value, Array

PROCS = 3
count = 0

def showdata(scalar, vector, label=''):
    ''' show the information in shared objects 
    count(global object: not shared within processes, each have their own copy)
    scalar(Value object: shared, acts as a single value)
    vector(Array object: shared, acts as a shared list)
    '''
    msg = "%-12s pid: %s, global: %s, scalar: %s, vector: %s"
    print(msg % (label, os.getpid(), count, scalar.value, list(vector)))

def update(scalar, vector):
    ''' add 1 to the shared objects '''
    global count
    count += 1
    scalar.value += 1
    for i in range(len(vector)): vector[i] += 1

if __name__ == '__main__':
    scalar = Value('i', 0)
    vector = Array('d', PROCS)

    showdata(scalar, vector, "Start value in parent")

    print("\nShowing data in child")
    # spawn child and show shared memory
    p = Process(target=showdata, args=(scalar, vector))
    p.start(); p.join()     # start and join

    print("\nUpdate in parent and show in child, serially")
    # update in parent, show in spawned process
    for i in range(PROCS):
        count += 1
        scalar.value += 1
        vector[i] += 1
        p = Process(target=showdata, args=(scalar, vector))
        p.start(); p.join()

    print("\nLoop2: Update in parent and show in child when run parallely")
    processes = []
    for i in range(PROCS):
        count +=1 
        scalar.value += 1
        vector[i] += 1
        p = Process(target=showdata, args=(scalar, vector))
        processes.append(p)
        p.start()
    for process in processes: process.join()
   
    print("\nLoop3: Update in children serially, show in parent")
    for i in range(PROCS):
        p = Process(target=update, args=(scalar, vector))
        p.start(); p.join()
    showdata(scalar, vector)

    print("\nLoop4: Update in children parallely, show in parent")
    processes = []
    for i in range(PROCS):
        p = Process(target=update, args=(scalar, vector))
        p.start()
        processes.append(p)
    for process in processes: process.join()

    # showing results
    showdata(scalar, vector)

