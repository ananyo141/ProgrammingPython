#!/usr/bin/env python3
# Find the differences between two directories, for directories, compare the
# filenames in each level, for files compare raw filecontents for absolute copy.

import os, dirdiff

BLKSIZE = 1024 * 1024 # 1MB

# get the same items in directory
def intersection(seq1:[str], seq2:[str]) -> [str]:
    ''' Return the items common in both seq1 and seq2 '''
    return [item for item in seq1 if item in seq2]

# compare directories and files
def comparetrees(dir1:str, dir2:str, verbose:bool=False, blksize:int=BLKSIZE) -> dict:
    ''' Compare all files and subdirectories in two directory 
    trees dir1 and dir2, and return a dict containing information
    of matching, differing and unique items in each level '''

    levelItems1 = os.listdir(dir1)
    levelItems2 = os.listdir(dir2)
    levelStat = dict(
        match     = [],
        differs   = [],
        unique    = []
    )

    if verbose: print()     # to avoid uneven newlines in case of optional printing
    if not (dirdiff.compareDirs(dir1, dir2, levelItems1, levelItems2)) and verbose:
        print("%s and %s differs" % (dir1, dir2))

    # compare file names lists
    if verbose: print(f"Comparing contents of {dir1} and {dir2}...")
    common = intersection(levelItems1, levelItems2)
    missed = common[:]      # alternative to common.copy()
    # compare files contents in common
    for filename in common:
        filepath1 = os.path.join(dir1, filename)
        filepath2 = os.path.join(dir2, filename)
        if os.path.isfile(filepath1) and os.path.isfile(filepath2):
            missed.remove(filename)
            # open both files and check byte by byte
            with open(filepath1, 'rb') as file1, open(filepath2, 'rb') as file2:
                while True:
                    chunk1 = file1.read(blksize)
                    chunk2 = file2.read(blksize)
                    if (not chunk1) and (not chunk2):
                        if verbose: print(f"{filename} matches")
                        levelStat['match'].append(filename)
                        break
                    if chunk1 != chunk2:
                        if verbose: print(f"{filename} differs")
                        levelStat['differs'].append(filename)
                        break

    # recur to compare common subdirectories
    for subdir in common:
        subdirpath1 = os.path.join(dir1, subdir)
        subdirpath2 = os.path.join(dir2, subdir)
        if os.path.isdir(subdirpath1) and os.path.isdir(subdirpath2):
            missed.remove(subdir)
            levelStat[subdir] = comparetrees(subdirpath1, subdirpath2, verbose, blksize)

    # mark unidentified items (both not dir or file)
    levelStat['missed'] = missed
    levelStat['unique'] = list(set(levelItems1) - set(levelItems2))
    
    return levelStat

# get and parse commandline args
if __name__ == '__main__':
    import argparse, json, sys

    parser = argparse.ArgumentParser()
    parser.add_argument('dir1',            help='Source directory')
    parser.add_argument('dir2',            help='Backup directory')
    parser.add_argument('-v', '--verbose', help='Verbose output',  action='store_true')
    parser.add_argument('-o', '--output',  help='Output stat json file', default=False)
    args = parser.parse_args()
    
    dir1, dir2 = map(os.path.abspath, (args.dir1, args.dir2))
    if not os.path.isdir(dir1) or not os.path.isdir(dir2):
        sys.exit("Invalid directory specified")

    if hasattr(os.path, 'samefile'):
        same = os.path.samefile(dir1, dir2)
    else:
        same = dir1 == dir2
    if same:
        sys.exit("Same directory specified")
    directoryStats = dict()
    directoryStats[os.path.basename(dir1)] = comparetrees(dir1, dir2, args.verbose)
    if args.output:
        with open(args.output, 'w') as outfile:
            json.dump(directoryStats, outfile, indent=4)

