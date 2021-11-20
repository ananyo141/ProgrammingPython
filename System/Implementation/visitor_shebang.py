#!/usr/bin/env python3
# Change the shebang lines in all the python files in
# a directory tree to new line

from visitor import FileVisitor

class ShebangFixer(FileVisitor):
    def __init__(self, context=None, trace=2):
        FileVisitor.__init__(self, context, trace)
        self.clist  = []
        self.ccount = 0
    def visitfile(self, filepath):
        FileVisitor.visitfile(self, filepath)
        if filepath.endswith(".py"):
            self.fixshebang(filepath)
    def fixshebang(self, filepath):
        lines = []
        with open(filepath) as pyfile:
            if pyfile.readline().startswith('#!'):
                lines = pyfile.readlines()
                self.clist.append(filepath)
                self.ccount += 1
        if lines:
            with open(filepath, 'w') as pyfile:
                pyfile.write(self.context+'\n' if self.context is not None else '\n')
                pyfile.writelines(lines)

if __name__ == '__main__':
    import argparse, os
    
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', nargs='?', help='Directory to change shebang', default=os.getcwd())
    parser.add_argument('change_to', nargs='?', help='Change string for shebang',   default='#!/usr/bin/env python3')
    parser.add_argument('-t', '--trace',        help='Trace script execution',      default=2, type=int)
    args = parser.parse_args()

    fixer = ShebangFixer(args.change_to, args.trace)
    fixer.run(args.directory)
    print('\n'+ '-'*60 + '\n')
    print(f"Fixed {fixer.ccount} out of {fixer.fcount} files")
    for change in fixer.clist: print(change)

