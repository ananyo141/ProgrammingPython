"Collect commandline options as dict"

def getopts(argv: list) -> dict:
    '''Get the commandline options as a dict and return'''

    opts = {}
    while argv:
        if argv[0][0] == '-':
            opts[argv[0]] = argv[1]
            argv = argv[2:]
        else:
            argv = argv[1:]
    
    return opts

if __name__ == '__main__':
    import sys
    parsed = getopts(sys.argv)
    print(parsed)
