#fork + exec combination
import os

parm = 0
while True:
    parm += 1
    pid = os.fork() # copy the process
    if pid == 0:    # for the child process
        print("Child %d" % os.getpid())
        os.execlp('python', 'python', 'child.py', str(parm)) # supply cmdline arg
        assert False, "Error creating new process"  # os.execlp call should not return
    else:           # for parent
        print("Spawned new child process %d" % pid)
        if input() == 'q': break

