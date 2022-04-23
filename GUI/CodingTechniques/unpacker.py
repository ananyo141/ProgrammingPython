#!/usr/bin/env python3

# Complementary script to unpack files made by packer.py
import os
from packer import MARKER

def unpack(ifile, prefix=''):
    for line in open(ifile, 'rb'):
        if line.startswith(MARKER.encode()):
            filename = line[len(MARKER):-1]
            if prefix:
                head, ext = os.path.split(filename)
                filename = os.path.join(head, prefix.encode() + ext)
            print(f'Creating {filename.decode()}...')
            outputfile = open(filename, 'wb')
        else:
            outputfile.write(line)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 1: 
        sys.exit("USAGE: " + sys.argv[0] + " PACKFILE")
    unpack(sys.argv[1])

