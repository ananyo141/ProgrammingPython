#!/usr/bin/env python3
# Compare directories at a single level and report differences

import os

# report the differences
def reportdiffs(unique1:[str], unique2:[str], dir1:str, dir2:str, verbose:bool=False) -> None:
    ''' Report to stdout the items unique to corresponding directories '''
    dir1, dir2 = map(os.path.abspath, (dir1, dir2))
    if not (unique1 or unique2):
        if verbose:
            print(f"{dir1} and {dir2} are identical")
        return
    if unique1 and verbose:
        print(f"Unique to {dir1}")
        for item in unique1:
            print(f"--> {item}")
    if unique2 and verbose:
        print(f"\nUnique to {dir2}")
        print(*(f"--> {item}" for item in unique2), sep='\n')

# single out the ones that are exclusive to a single directory
def difference(seq1:[str], seq2:[str]) -> [str]:
    ''' Find and return 'names' present in seq1 exclusively
    that are not present in seq2 '''
    return [item for item in seq1 if item not in seq2]

# compare dirs if they contain the same 'item' names
def compareDirs(dir1:str, dir2:str, files1:list=None, files2:list=None, verbose:bool=False) -> bool:
    ''' Compare the two directories dir1 and dir2, check
    if both contain the same 'item names' and report 
    the unique items '''
    
    files1 = os.listdir(dir1) if files1 is None else files1
    files2 = os.listdir(dir2) if files2 is None else files2
    unique1 = difference(files1, files2)
    unique2 = difference(files2, files1)

    reportdiffs(unique1, unique2, dir1, dir2, verbose)
    return not (unique1 or unique2)             # false if one unique, true otherwise

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('dir1', help='First directory')
    parser.add_argument('dir2', help='Second directory')
    parser.add_argument('-v', '--verbose', help='Verbose output')
    args = parser.parse_args()

    if not os.path.isdir(args.dir1): raise SystemExit(f"{args.dir1} doesn't exist")
    if not os.path.isdir(args.dir2): raise SystemExit(f"{args.dir2} doesn't exist")

    compareDirs(args.dir1, args.dir2, verbose=True)

