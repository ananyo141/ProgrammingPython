#!/usr/bin/env python3

# Simple utility to pack multiple files
MARKER = '*' * 20 + '=> '

def pack(ofile: str, ifiles: list[str]) -> str:
    " Pack a list of files into a resulting output file "

    with open(ofile, 'wb') as outputfile:
        for filename in ifiles:
            print(f'Packing {filename}...')
            outputfile.write(f"{MARKER}{filename}\n".encode())
            try:
                for line in open(filename, 'rb'):
                    outputfile.write(line)
            except: 
                print(f"Unable to write {filename}")
                continue

    return ofile

if __name__ == '__main__':
    import sys, glob
    if len(sys.argv) < 2: sys.exit("USAGE: " + sys.argv[0] + " OUTFILE FILE(s) [...]")
    packlist = []
    for filepattern in sys.argv[2:]:
        packlist.append(*glob.glob(filepattern))
    pack(sys.argv[1], packlist)

