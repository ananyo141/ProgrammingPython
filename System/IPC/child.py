import os, sys
print("Hello from child %d %s" % (os.getpid(), sys.argv[1]))
