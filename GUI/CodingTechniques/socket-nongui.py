from socket_stream_redirect0 import redirectOut

import sys, time

sockfile = redirectOut() if len(sys.argv) > 1 else sys.stdout

while True:
    print(time.asctime(), file=sockfile)
    sockfile.flush()
    time.sleep(2)

