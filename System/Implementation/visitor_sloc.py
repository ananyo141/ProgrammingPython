#!/usr/bin/env python3
# Count the source lines of code for program files and python files

import os
from visitor import FileVisitor

class ListByExt(FileVisitor):
    extensions = []                # expandable by subclassing
    def __init__(self, trace=2):
        FileVisitor.__init__(self, trace)
        self.srcfiles = self.srclines = 0  # count the running total
        # a dict to hold per-extension record
        self.sloc_stats = {ext: dict(files=0, lines=0) for ext in self.extensions}   

    def visitfile(self, filepath):
        for ext in self.extensions:
            if filepath.endswith(ext):
                self.visitsource(ext, filepath)     # if match found
                break                               # execute match code

    def visitsource(self, ext, filepath):
        if self.trace > 0: print(os.path.basename(filepath))
        lines = sum(+1 for line in open(filepath, 'rb'))
        self.srclines += lines
        self.srcfiles += 1

        self.sloc_stats[ext]['lines'] += lines
        self.sloc_stats[ext]['files'] += 1

class PyFiles(ListByExt):
    extensions = ['.py', '.pyw']

class SourceLines(ListByExt):
    extensions = ['.py', '.pyw', '.cgi', '.html', '.c', '.cxx', '.h', '.i']

if __name__ == '__main__':
    import sys, pprint

    walker = SourceLines(trace=0)
    walker.run(sys.argv[1])
    print("Visited %d files and %d dirs" % (walker.fcount, walker.dcount))
    print('-'*50)
    print("Source files => %d, lines => %d" % (walker.srcfiles, walker.srclines))
    print("By types:")
    pprint.pprint(walker.sloc_stats)

    print('\nCheck sums:', end=' ')
    # sum of lines
    #print(sum(exc['lines'] for exc in walker.sloc_stats.values()))
    # sum of files
    #print(sum(exc['files'] for exc in walker.sloc_stats.values()))
    # a python only walk
    pywalker = PyFiles(trace=0)
    pywalker.run(sys.argv[1])
    print("Source files => %d, lines => %d" % (pywalker.srcfiles, pywalker.srclines))

