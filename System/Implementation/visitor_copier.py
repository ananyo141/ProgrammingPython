#!/usr/bin/env python3
# Write the copier utility using visitor class

import os
from visitor import FileVisitor
from copier import copyFile

class CopyVisitor(FileVisitor):
    def __init__(self, fromDir, toDir, trace=True):
        FileVisitor.__init__(self, trace)
        self.fromDir = fromDir
        self.toDir   = toDir
        self.fromInd = len(self.fromDir) + 1    # fixed index of src directory
    def run(self, reset=True):
        FileVisitor.run(self, self.fromDir, reset)
    def visitdir(self, dirpath):
        toDirpath = os.path.join(self.toDir, dirpath[self.fromInd:])
        if self.trace: print(dirpath, '=>', toDirpath)
        os.makedirs(toDirpath, exist_ok=True)
    def visitfile(self, filepath):
        toFilepath = os.path.join(self.toDir, filepath[self.fromInd:])
        if self.trace: print(filepath, '=>', toFilepath)
        copyFile(filepath, toFilepath)

if __name__ == '__main__':
    import sys
    try:
        fromDir, toDir = sys.argv[1:]
    except ValueError:
        sys.exit("Usage: visitor_copier.py FROMDIR TODIR")
    
    copierwalker = CopyVisitor(fromDir, toDir)
    copierwalker.run()

    print("\nCopied %s to %s" % (copierwalker.fromDir, copierwalker.toDir))
    print("Copied %d files and %d directories" % (copierwalker.fcount, copierwalker.dcount))

