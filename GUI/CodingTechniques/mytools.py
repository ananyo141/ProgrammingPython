# Use the shellgui templates designed in shellgui.py

import sys, os
sys.path.append('../../System/Implementation')

from split import split
from join  import join
from shellgui import ListShellGui, DictShellGui

splitFunc = lambda: split(__file__, os.curdir)
joinFunc  = lambda: join(os.path.join(os.curdir, 'Splits'))

class TestShellList(ListShellGui):
    def __init__(self):
        self.myMenu = (('Split', splitFunc),
                ('Join',  joinFunc))
        ListShellGui.__init__(self)

    def forToolbar(self, label):
        return label == 'Split'

class TestShellDict(DictShellGui):
    def __init__(self):
        self.myMenu = {'Split': splitFunc,
                       'Join' : joinFunc}
        DictShellGui.__init__(self)

    def forToolbar(self, label):
        return label == 'Join'

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'list':
        TestShellList().mainloop()
    else:
        TestShellDict().mainloop()

