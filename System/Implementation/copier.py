#!/usr/bin/env python3
import os

MAXSIZE = 1000000    # bytes
BLKSIZE = 1024 * 500 # KB

def copyFile(pathFrom: str, pathTo: str, maxsize: int = MAXSIZE) -> None:
    ''' Copy a file from pathFrom to pathFile '''
    if os.path.getsize(pathFrom) <= MAXSIZE:
        open(pathTo, 'wb').write(open(pathFrom, 'rb').read())
    else:
        with open(pathFrom, 'rb') as infile, open(pathTo, 'wb') as outfile:
            while True:
                chunk = infile.read(BLKSIZE)
                if not chunk: break
                outfile.write(chunk)

def copyTree(dirFrom: str, dirTo: str, verbose: bool = False) -> tuple:
    ''' Copy the directory tree from 'dirFrom' to 'dirTo' '''
    dirCopied = fileCopied = 0
    for dirname, subdirs, filenames in os.walk(dirFrom):
        dstDir = os.path.join(dirTo, os.path.relpath(dirname, dirFrom))
        if not os.path.exists(dstDir):
            os.mkdir(dstDir)
        for filename in filenames:
            fromFile = os.path.join(dirname, filename)
            toFile   = os.path.join(dstDir,  filename)
            try:
                if verbose: print(f"Copying '{fromFile}' to '{toFile}'...")
                copyFile(fromFile, toFile)
            except Exception as exc:
                print(f"Error while copying,", str(exc), "skipping--")
                continue
            fileCopied += 1
        dirCopied += 1
    return dirCopied, fileCopied

if __name__ == '__main__':
    import argparse, time, sys
    
    parser = argparse.ArgumentParser()
    parser.add_argument('source',          help='Source')
    parser.add_argument('destination',     help='Destination')
    parser.add_argument('-v', '--verbose', help='Verbose output',  action='store_true')
    parser.add_argument('-f', '--force',   help='Force overwrite', action='store_true')
    args = parser.parse_args()

    if not os.path.isdir(args.source):
        sys.exit(f"{args.source} isn't a valid source")
    if os.path.exists(args.destination) and not args.force:
        print(f"Warning: {args.destination} already exists.\nComparing...")
        if hasattr(os.path, 'samefile'):
            same = os.path.samefile(args.source, args.destination)
        else:
            same = os.path.abspath(args.source) == os.path.abspath(args.destination)
        if same:
            sys.exit("Error: Source and destination can't be same")

    start = time.time()
    dirsCopied, filesCopied = copyTree(args.source, args.destination, args.verbose)
    print(f"Copied {filesCopied} files and {dirsCopied} directories\n"
          f"from {args.source} to {args.destination} in {time.time() - start:.3f} seconds")

