import sys, signal, time

def now(): return time.asctime()

def onSignal(signalNum, stackframe):
    print("Got signal %d on %s" % (signalNum, now()))

print("Setting signal %d at %s\n" % (signal.SIGALRM, now()))
signal.signal(signal.SIGALRM, onSignal)  # install handler for SIGALARM, gets reinstated
while True:
    signal.alarm(5)                      # send SIGALRM to itself in 5 seconds
    signal.pause()

