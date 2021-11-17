#!/usr/bin/env python3
# Search for a given string in a directory tree

import os

listonly = False
textext  = ('.txt', '.py', '.pyw', '.c', '.h')

def searcher(directory: str, searchkey: str) -> None:
    ''' Search all the compatible text files in the
    given directory for the given search key '''
    
    # keep track of files and directories visited
    global findCount, visitCount
    findCount = visitCount = 0

    for dirname, subdirs, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirname, filename)
            visitFile(filepath, searchkey)

def visitFile(filepath: str, searchkey: str) -> None:
    ''' Visit each file and search it's contents if 
    it's extension is in the valid extensions tuple '''

    global findCount, visitCount
    print(f"{visitCount+1} => {repr(filepath)}")
    if not listonly:
        try:
            if os.path.splitext(filepath)[1] not in textext:
                print(f"Skipping {repr(filepath)}")
            elif searchkey in open(filepath).read():
                print(f"Found {repr(searchkey)} in {repr(filepath)}\n")
                findCount += 1
        except Exception as exc:
            print("Error", str(exc), sep = '\n')

    visitCount += 1

if __name__ == '__main__':
    import sys
    try:
        dirname, searchkey = sys.argv[1:]
    except ValueError:
        sys.exit(f"Usage: search_all <dirname> <searchkey>")

    searcher(dirname, searchkey)
    print(f"\nFound {repr(searchkey)} in {findCount} files out of {visitCount} files visited")

