"""
Implement a webserver that acts as a mediator between the 
browser and python script
"""

import os
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'    # where html files and cgi-bin script directory live
port = 80       # default http://localhost/, else http://localhost:xxxx/

os.chdir(webdir)                                        # run in HTML root dir
srvraddr = ("", port)                                   # my hostname, portnumber
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler) 
srvrobj.serve_forever()                                 # run as perpetual daemon
