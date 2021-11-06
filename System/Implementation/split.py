#!/usr/bin/env python3
# Split files portably
import os, shutil

KB = 1024      # bytes
MB = KB * 1000 # KiloBytes
CHUNKSIZE = 5 * MB

def split(inputFilename: str, outputDir: str, chunksize: int=CHUNKSIZE) -> int:
    ''' Split the inputFile into required number of chunks and return the 
        number of parts created '''
    outputDir = os.path.join(outputDir, 'Splits') # repurpose outputdir to save
    if os.path.exists(outputDir):                 # contents in nested directory
        shutil.rmtree(outputDir)          # remove the directory if exists
    os.mkdir(outputDir)                   # create a clean directory
    part = 0
    inputFileStem = os.path.basename(inputFilename)
    with open(inputFilename, 'rb') as inputFile:
        while True:
            chunk = inputFile.read(chunksize)
            if not chunk: break           # break if read finishes
            outputFilename = os.path.join(outputDir, f"{inputFileStem}.split{part+1:03d}")
            with open(outputFilename, 'wb') as outputFile:
                outputFile.write(chunk)
            part += 1
    return part

if __name__ == '__main__': 
    import tkinter.filedialog, argparse, sys
    if len(sys.argv) > 1:       # command-line mode
        parser = argparse.ArgumentParser()
        parser.add_argument('source',             help='Select input file')
        parser.add_argument('-d', '--output-dir', help='Select output directory', default=os.getcwd())
        parser.add_argument('-c', '--chunk-size', help='Select chunk size',       default=CHUNKSIZE,
                                                                                  type=int)
        args = parser.parse_args()
        source, outputDir = map(os.path.normpath, (args.source, args.output_dir))
        chunksize = args.chunk_size
    else:                       # interactive-mode
        source = tkinter.filedialog.askopenfilename(title='Select file to split')
        outputDir = tkinter.filedialog.askdirectory()
        if not source or not outputDir:
            sys.exit("Both source and output directory required")
        try:
            chunksize = int(input("Enter chunk size: "))
        except ValueError:
            sys.exit("Expected integer input")
        source, outputDir = map(os.path.normpath, (source, outputDir)) # convert to windows-friendly

    print(f"Splitting from '{os.path.abspath(source)}' to\n"
          f"'{os.path.abspath(outputDir)}' by {chunksize} bytes")
    try:
        numParts = split(source, outputDir, chunksize)
    except Exception as e:
        print("Error during split", str(e), sep='\n')
    else:
        print(f"Split finished, {numParts} parts are in {os.path.abspath(outputDir)}")
        assert numParts <= 9999, "Too many parts to join"              # join will fail for 5-digit parts
    if len(sys.argv) == 0: input("Press enter to exit")

