"""File like objects with read and write attributes to act as the file stream buffers instead of real files"""

import sys

class Input:
    def __init__(self, input = ''):
        self.text = input
    def read(self, size=None):
        if size == None: # ie full text is reqd
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:size], self.text[size:]
        return res
    def readline(self):
        eoln = self.text.find('\n')
        if eoln == -1:
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:eoln + 1], self.text[eoln + 1:]
        return res

class Output:
    def __init__(self):
        self.text = ''
    def write(self, text):
        self.text += text
    def writelines(self, lines):
        for line in lines: self.write(line)

def redirect(function, pargs, kwargs, input):
    savestreams = sys.stdin, sys.stdout     # save the streams to be reinstated after function call return
    sys.stdin = Input(input)
    sys.stdout = Output()
    try:
        returnVal = function(*pargs, **kwargs)
        output = sys.stdout.text
    finally:
        sys.stdin, sys.stdout = savestreams # restore the streams
    
    return returnVal, output
