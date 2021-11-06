#!/usr/bin/env python3
# Test scripts and save run results in files

import os, sys, glob, argparse

def buildTestDir(directories: [str]) -> None:
    ''' build test directory folders in the given directory root '''
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def main():
    DIR_STR = dict(
        SCRIPT_DIR = 'Scripts',
        ARGS_DIR   = 'Args',
        ERRORS_DIR = 'Errors',
        INPUT_DIR  = 'Inputs',
        OUTPUT_DIR = 'Outputs'
    )

    parser = argparse.ArgumentParser()
    parser.add_argument('directory',          help='Script Testing Directory (Root)'                  )
    parser.add_argument('-c', '--create-dir', help='Create the testing directory', action='store_true')
    parser.add_argument('-f', '--force-gen',  help='Force generate output',        action='store_true')
    args = parser.parse_args()

    for dirname, dirvalue in DIR_STR.items():
        DIR_STR[dirname] = os.path.join(args.directory, dirvalue)
    if args.create_dir:
        print("Creating testing directory...")
        buildTestDir(list(DIR_STR.values()))
        print("Directory created at", os.path.abspath(args.directory))
        sys.exit(0)

    if any(not os.path.exists(dirname) for dirname in DIR_STR.values()):
        sys.exit("Complete directory structure doesn't exist;\n"
                 "Create or use '-c' flag to make one")
    # Find all script files in test directory, (root)
    scripts = glob.glob(os.path.join(DIR_STR['SCRIPT_DIR'], '*.py'))
    scripts.sort()
    for script_path in scripts:
        script_name = os.path.basename(script_path)

        # For every test script, get input and argument list
        input_file = os.path.join(DIR_STR['INPUT_DIR'], script_name.replace('.py','.in'))
        input_data = open(input_file).read() if os.path.exists(input_file) else b''
        
        arg_file = os.path.join(DIR_STR['ARGS_DIR'], script_name.replace('.py','.args'))
        arg_data = open(arg_file).read() if os.path.exists(arg_file) else ''
    # locate output and error, scrub prior results
    # run test with redirected streams
    # analyze results

if __name__ == '__main__':
    main()

