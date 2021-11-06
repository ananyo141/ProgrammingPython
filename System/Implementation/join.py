#!/usr/bin/env python3
# Join the split files back to original form.
import os

CHUNKSIZE = 1024 * 5 #5KB

def join(src_dir: str) -> str:
    ''' Join the splitted files into its original form and
        return the recreated filename'''
    
    splits = os.listdir(src_dir)
    splits.sort()               # sort the list to make files according to part number
    splitPresent = False
    # deduce the original filename
    for item in splits:
        itemBase, itemExt = os.path.splitext(item)
        if '.split' in itemExt:
            splitPresent = True
            outputFilename = itemBase
            break
    if not splitPresent: raise Exception("No splits found")
    outputFilePath = os.path.join(src_dir, outputFilename)
    with open(outputFilePath, 'wb') as outputFile:
        for split in splits:
            splitPath = os.path.join(src_dir, split)
            if not os.path.isfile(splitPath) or \
                '.split' not in os.path.splitext(splitPath)[1]: continue
            print(f"Joining {split}...")
            with open(splitPath, 'rb') as inputFile:
                while True:
                    chunk = inputFile.read(CHUNKSIZE)   # avoid loading file all at once
                    if not chunk: break
                    outputFile.write(chunk)
    return outputFilePath

if __name__ == '__main__':
    import tkinter.filedialog, sys
    if len(sys.argv) > 1:
        if sys.argv[1] == '-h':
            print("Usage: join.py [src_dir]")
            sys.exit(0)
        interactive = False
        src_dir = sys.argv[1]
    else:
        interactive = True
        src_dir = input("Enter source directory: ")
    if not os.path.exists(src_dir):
        sys.exit("Invalid directory")
    processedFile = join(src_dir)
    print(f"File successfully recreated at {os.path.abspath(processedFile)}")
    if interactive: input("Press Enter to exit")

