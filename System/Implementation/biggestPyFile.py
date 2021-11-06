# Find the biggest file in the given directory
import os, sys, argparse, time, json

def bytesToKB(size: int) -> float:
    ''' convert bytes to KB '''
    return round(size / 1024, 3)

def tryPrint(message: str) -> None:
    ''' Try to print the given string to stdout,
    avoid script crash due to unicode errors '''
    try:
        print(message)
    except UnicodeDecodeError:
        print(message.encode()) # else print encoded form 

def filestatPrinter(filepath: str, size: float, lines: int) -> None:
    ''' Print the file stats to stdout '''
    print("File: %s\n"
          "Size: %.3fKB\n"
          "Lines: %d\n"
          % (filepath, size, lines))

def jsonBuild(directory: str, extension: str) -> dict:
    ''' build a json type dictionary containing file stats,
    with every subdirectory nested a level deeper using recursion '''
    dirstats = dict()
    subdirs = set()
    # Search the directory
    for item in os.listdir(directory):
        itempath = os.path.join(directory, item)
        if os.path.isdir(itempath):
            subdirs.add(itempath)
        elif os.path.isfile(itempath) and os.path.splitext(itempath)[1] == extension:
            try:
                size = bytesToKB(os.path.getsize(itempath))
            except os.error:
                print("Unable to get size of %s, Continuing..." % itempath)
                continue
            lines = sum(+1 for line in open(itempath, 'rb'))
            dirstats[item] = {'size': size, 'lines': lines}
    # Add the subdirs in recursion in order to give structure to
    # the json file
    for subdir in subdirs:
        subdirData = jsonBuild(subdir, extension)
        if subdirData:
            dirstats[os.path.basename(subdir)] = subdirData
    return dirstats

def main():
    # Parse command line arguments, else give default values
    parser = argparse.ArgumentParser()       # flag in 'module' to search PYTHONPATH also, store bool instead of value
    parser.add_argument('-m', '--module',    help='Search the python system module path',       action='store_true') # default False
    parser.add_argument('-d', '--directory', help='Select the directory to perform the search', nargs='*', default=[os.getcwd()])
    parser.add_argument('-e', '--extension', help='Select the extension to search',             default='.py')
    parser.add_argument('-o', '--output',    help='Select output file path (.json)',            default='')
    parser.add_argument('-t', '--trace',     help='Trace the execution of the program\n'
                                                  '0: Turn off tracing\n'
                                                  '1: Display the directories\n'
                                                  '2: Display the files searched\n',            type=int, choices=(0,1,2),
                                                                                                default=0)
    args = parser.parse_args()
    directories = args.directory + sys.path if args.module else args.directory

    visited = set()
    dirstats = dict()
    filestats = list()
    # Search the directory
    for directory in directories: 
       if args.output:     # Create json data
            dirstats[directory] = jsonBuild(directory, args.extension)
       for dirname, subdirs, filenames in os.walk(directory):
            dirname = os.path.normpath(dirname)     # fix path for windows
            dirname = os.path.normcase(dirname)     # fix case for windows
            if args.trace > 0: tryPrint('\n' + dirname)
            if dirname in visited: 
                print("Skipping %s" % directory)
                continue
            visited.add(dirname)
            for filename in filenames:
                if not filename.endswith(args.extension):
                    continue
                if args.trace > 1: tryPrint(filename)
                filepath = os.path.join(dirname, filename)
                try:
                    size = bytesToKB(os.path.getsize(filepath))
                except os.error:
                    print("Unable to get size of", filepath)
                with open(filepath, 'rb') as file:
                    lines = sum(+1 for line in file)
                filestats.append((filepath, size, lines))

    # Print the results
    print(" According to size ".center(50, '*'))
    for firstThree in sorted(filestats, key=lambda x: x[1])[:3]:
        filestatPrinter(*firstThree)
    print(" Size (Last Three) ".center(50, '*'))
    for lastThree in sorted(filestats, key=lambda x: x[1])[-3:]:
        filestatPrinter(*lastThree)

    print(" According to lines ".center(50, '*'))
    for firstThree in sorted(filestats, key=lambda x: x[2])[:3]:
        filestatPrinter(*firstThree)
    print(" Lines (Last Three) ".center(50, '*'))
    for lastThree in sorted(filestats, key=lambda x: x[2])[-3:]:
        filestatPrinter(*lastThree)
    
    if args.output:
        with open(args.output, 'w') as jsonFile:
            json.dump(dirstats, jsonFile, indent=4)

if __name__ == '__main__': main()

