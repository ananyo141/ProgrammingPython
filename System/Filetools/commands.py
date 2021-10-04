commands = {'*': 'Ms.', '+': 'Mr'}

class UnknownCommand(Exception): pass

def processLine(line):
    try:
        print(commands[line[0]], line[1:-1])    # ignore newline
    except KeyError:
        raise UnknownCommand(line)


if __name__ == '__main__':
    processLine('*This is ok\n')
    processLine('Not ok')
