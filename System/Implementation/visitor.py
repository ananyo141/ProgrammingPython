#!/usr/bin/env python3
# A general purpose directory walker that abstracts and encapsulates
# the directory walking logic and acts as a customizable and expandable
# library and base class

import os

class FileVisitor:
    def __init__(self, context=None, trace=2):
        self.fcount  = 0     # files visited
        self.dcount  = 0     # directories visited
        self.context = context  # save any optional context (eg, search keys)
        self.trace   = trace    # 0=None, 1=Dirs, 2=Files also

    def run(self, root_dir=os.curdir, reset=True):
        ''' Traverse the entire directory tree from the 
        given root '''
        # Only the barebones directory traversal logic
        if reset: self.reset()
        for dirname, subdirs, filenames in os.walk(root_dir):
            self.visitdir(dirname)
            for filename in filenames:
                filepath = os.path.join(dirname, filename)
                self.visitfile(filepath)
                self.fcount += 1
            self.dcount += 1

    def reset(self):
        ''' Reset the file and directory counter '''
        self.fcount = self.dcount = 0

    def visitdir(self, dirpath):
        ''' Visit each directory and print name '''
        if self.trace > 0: print(dirpath)

    def visitfile(self, filepath):
        ''' Visit each file and print filename '''
        if self.trace > 1: print(filepath)

class SearchVisitor(FileVisitor):
    ''' A barebones searcher with extensible methods '''
    skipexts = []
    testexts = ['.txt', '.py', '.pyw', '.html', '.c', '.h']
    #skipexts = ['.gif', '.jpg', '.pyc', '.o', '.a', '.exe', '.out']

    def __init__(self, search_key, trace=2):
        FileVisitor.__init__(self, search_key, trace)
        self.scount = 0
    
    def reset(self, searchCount=True):
        FileVisitor.reset(self)
        if searchCount:
            self.scount = 0

    def candidate(self, filename):              # can be overridden to determine
        ext = os.path.splitext(filename)[1]     # possible filetype for inspection by
        if self.testexts:                       # different methods, like mimetypes
            return ext in self.testexts
        else:
            return ext not in self.skipexts

    def visitfile(self, filepath):
        FileVisitor.visitfile(self, filepath)
        if self.candidate(filepath):
            try:
                text = open(filepath).read()
            except Exception as exc:
                print("Unable to read file '%s', %s\nSkipping...." % (filepath, str(exc)))
            else:
                if self.context in text:
                    self.visitmatch(filepath, text)
                    self.scount += 1
        else:
            if self.trace > 1: print("Skipping", repr(filepath))

    def visitmatch(self, filepath, text):
        if self.trace > 1:
            print("Found %s in %s" % (self.context, repr(filepath)))


if __name__ == '__main__':
    # Self testing logic
    import sys
    testmask  = sys.argv[1]
    directory = sys.argv[2]

    dolist   = 1  # 001 in binary
    dosearch = 2  # 010 in binary
    dotest   = 4  # for next test (reserved)
    # so 3 i.e, 011 in binary matches 
    # both dolist and dosearch tests

    def selftest(testmask: int) -> None:
        ''' Self testing the two classes '''

        if testmask & dolist:
            visitor = FileVisitor(trace=2)
            visitor.run(directory)
            print("\nVisited %d files and %d directories" % (visitor.fcount, visitor.dcount))

        if testmask & dosearch:
            searcher = SearchVisitor(sys.argv[3], trace=0)
            searcher.run(directory)
            print("\nFound in %d files, visited %d" % (searcher.scount, searcher.fcount))

    selftest(int(testmask))
