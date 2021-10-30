import os, sys

for i in range(10):
    if sys.platform[:3] == 'win32':
        pypath = sys.executable
        os.spawnv(os.P_NOWAIT, pypath, ('python', 'child.py', str(i)))
    else:
        pid = os.fork()
        if pid != 0:    # parent
            print("Process spawned", pid)
        else:
            os.execlp('python', 'python', 'child.py', str(i))

print("Main process exiting")

