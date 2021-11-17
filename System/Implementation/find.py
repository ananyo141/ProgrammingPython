#!/usr/bin/env python3
# A find utility that searches the entire directory tree to find filenames
# matching given pattern

import fnmatch, os

def find(pattern, startdir=os.curdir):
    ''' Find file and directory names matching given (Unix-like) pattern.
    Generator expression yields result instead of waiting for process to exit '''
    for dirname, subdirs, filenames in os.walk(startdir):
        for name in subdirs + filenames:
            if fnmatch.fnmatch(name, pattern):
                fullpath = os.path.join(dirname, name)
                yield fullpath

def findlist(pattern, startdir=os.curdir, sort=False):
    ''' Return a list of matching file and dirnames '''
    match = list(find(pattern, startdir))
    if sort: match.sort()
    return match

if __name__=='__main__':
    import sys
    try:
        pattern, *directories = sys.argv[1:]
    except ValueError:
        sys.exit("Usage: find.py {pattern} {directories...}")

    directories = [os.curdir] if not directories else directories
    for directory in directories:
        print('-' * 40, f'\nSearching {os.path.abspath(directory)}\n')
        for name in find(pattern, directory): 
            print(name)

