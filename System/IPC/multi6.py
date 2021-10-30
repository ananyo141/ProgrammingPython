import os
from multiprocessing import Pool 

# instead of discrete tasks for each process,
# Pool makes the processes work a common task

def powers(x):
    print(os.getpid())
    return 2 ** x

if __name__ == '__main__':
    workers = Pool(processes=5)

    results = workers.map(powers, [2]*100)
    print(results[:16])    # print first 16 results
    print(results[-2:])    # print last two results

    results = workers.map(powers, range(100))
    print(results[:16])    # print first 16 results
    print(results[-2:])    # print last two results
    print("Parent process exit")

