# create a spawn function that forks a child process and interlaces their stdin
# and stdout

import os, sys

def spawn(prog, *args):
    stdinFd = sys.stdin.fileno()
    stdoutFd = sys.stdout.fileno()

    parentStdin, childStdout = os.pipe()
    childStdin, parentStdout = os.pipe()
    pid = os.fork()
    if pid:          # if parent
        # close the unused ends of pipe
        os.close(childStdin)
        os.close(childStdout)
        # change the standard streams with the pipes
        os.dup2(parentStdin, stdinFd)
        os.dup2(parentStdout, stdoutFd)
    else:            # if child
        # close the unused ends of pipe
        os.close(parentStdin)
        os.close(parentStdout)
        # change the standard streams with the pipes
        os.dup2(childStdin, stdinFd)
        os.dup2(childStdout, stdoutFd)
        args = (prog,) + args
        # overlay the child process with new program and arguments
        os.execvp(prog, args)
        assert False, 'execvp failed'       # should never execute if exec succeeded


if __name__ == '__main__':
    mypid = os.getpid()
    spawn('python', 'pipes-testchild.py', 'spam')   # fork child program

    print("Hello 1 from parent", mypid) # stdout is redirected to pipe
    sys.stdout.flush()                  # to avoid deadlock
    reply = input()
    sys.stderr.write("Parent got [%s]\n" % reply) # stderr is not tied to pipe

    print("Hello 2 from parent", mypid)
    sys.stdout.flush()
    reply = input()
    sys.stderr.write("Parent got [%s]\n" % reply[:-1]) # stderr is not tied to pipe
    
