"""
split interactively page a string or file or text to stdout (support redirection) and still be able to take command from stdin
"""
import sys

def getreply():
    """Read a reply key from an interactive user 
    even if stdin is redirected"""

    if sys.stdin.isatty():              # if stdin is console that is not redirected
        return input('? ').encode()
    else:
        if sys.platform[:3] == 'win':
            import msvcrt
            msvcrt.putch(b'?')
            key = msvcrt.getche()
            msvcrt.putch(b'\n')         # the '\n' is not reflected by getche()
            return key
        elif sys.platform == 'linux':
            open('/dev/tty').readline()[:-1]
        
def more(text, numlines=15):
    """Display the text numlines lines per page to stdout and prompt the user 
    to display more even if stdin is redirected"""
            
    lines = text.splitlines()
    while lines:
        chunk = lines[:15]
        lines = lines[15:]
        for line in chunk: print(line)
        if lines and getreply() not in [b'Y', b'y']: break
    
if __name__ == '__main__':
    if len(sys.argv) == 1:
        more(sys.stdin.read())          # if no files specified at cmd line, read from stdin
    else:
        more(open(sys.argv[1]).read())  # else read from file
