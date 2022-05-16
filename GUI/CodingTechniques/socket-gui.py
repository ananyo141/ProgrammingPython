import os
from tkinter import Tk
from guiStreams import GuiOutput
from socket import *
from socket_stream_redirect0 import PORT

# Act as the server
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', PORT))
sock.listen(5)

print('starting client')
os.system('/usr/bin/env python3 socket-nongui.py -gui &')

print('accepting')
conn, addr = sock.accept()
conn.setblocking(False)
print('accepted')

root = Tk()
output = GuiOutput(root)

def checkoutput():
    try:
        msg = conn.recv(1024)
        print(msg, file=output)
    except error:
        output.write('No message\n')
    root.after(1000, checkoutput)

checkoutput()
root.mainloop()

