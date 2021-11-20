#!/usr/bin/env python3
# Use visitor module classes to traverse directory and 
# open matching files in vim for editing

import os
from visitor import SearchVisitor 

class EditVisitor(SearchVisitor):

    editor = "/usr/bin/vim"

    def visitmatch(self, filepath, text):
        SearchVisitor.visitmatch(self, filepath, text)
        os.system('%s %s' % (self.editor, filepath))

if __name__ == '__main__':
    import sys

    editor = EditVisitor(sys.argv[1], trace=0)
    editor.run('.' if len(sys.argv) < 3 else sys.argv[2])
    print("\nEdited %d files out of %d files" % (editor.scount, editor.fcount))

