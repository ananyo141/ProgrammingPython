import signal, time, sys

def now(): return time.ctime()

def onSignal(sigNum, stackframe):
    print("Signal %d received at %s" % (sigNum, now()))

signalNum = int(sys.argv[1])
signal.signal(signalNum, onSignal)
while True: signal.pause()

