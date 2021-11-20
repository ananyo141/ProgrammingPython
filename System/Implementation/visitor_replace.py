#!/usr/bin/env python3
# Use searchvisitor class to apply global search and replace
# on files containing a given string to another string

from visitor import SearchVisitor

class ReplaceVisitor(SearchVisitor):
    def __init__(self, fromStr, toStr, listonly=False, trace=2):
        self.changed = []
        self.listonly = listonly
        self.toStr = toStr
        SearchVisitor.__init__(self, fromStr, trace)

    def visitmatch(self, filepath, text):
        ''' Perform global search-and-replace of the
        fromStr to toStr and save changes to file '''
        SearchVisitor.visitmatch(self, filepath, text)
        if not self.listonly:
            text = text.replace(self.context, self.toStr)
            open(filepath, 'w').write(text)
            self.changed.append(filepath)

if __name__ == '__main__':
    import sys

    try:
        fromStr, toStr, dirname = sys.argv[1:]
    except ValueError:
        sys.exit("Usage: visitor_replace.py from_str to_str directory")

    listonly = input("List only?: ").lower() == 'y'
    replacer = ReplaceVisitor(fromStr, toStr, listonly)
    if listonly or input('Proceed?: ').lower() == 'y':
        replacer.run(dirname)
        action = 'Found' if listonly else 'Changed'
        print('\n' + '*'*60 + '\n')
        print('%s %d files out of %d visited' % (action, len(replacer.changed), replacer.fcount))
        for change in replacer.changed: print(change)

