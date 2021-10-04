import sys

def filter_files(filename, function):
    with open(filename) as input, open(filename + '.out', 'w') as output:
        for line in input:
            output.write(function(line))

def filter_stream(function):
    for line in sys.stdin:
        sys.stdout.write(function(line))

if __name__ == '__main__':
    filter_stream(lambda line: line)
