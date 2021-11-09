#!/usr/bin/env python3
# Test scripts and save run results in files

import os, sys, glob, argparse, time
from subprocess import Popen, PIPE

def buildTestDir(directories: [str]) -> None:
    ''' build test directory folders in the given directory root '''
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def main():
    # dict data structure to hold the different folder names, dynamically
    # changes the contents to full pathnames during program execution
    DIR_STR = dict(
        SCRIPT_DIR = 'Scripts',
        ARGS_DIR   = 'Args',
        ERRORS_DIR = 'Errors',
        INPUT_DIR  = 'Inputs',
        OUTPUT_DIR = 'Outputs'
    )

    # Parse commandline arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('directory',          help='Script Testing Directory(Root)')
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
    scripts = glob.glob(os.path.join(DIR_STR['SCRIPT_DIR'], '*.py'))    # full pathnames of scripts
    scripts.sort()
    num_fails = 0
    print("Initiating testing for %s at \n%s\n" % (DIR_STR['SCRIPT_DIR'], time.asctime()))
    for script_path in scripts:
        script_name = os.path.basename(script_path)

        # For every test script, get input and argument list
        input_file = os.path.join(DIR_STR['INPUT_DIR'], script_name.replace('.py','.in'))
        input_data = open(input_file, 'rb').read() if os.path.exists(input_file) else b''
        
        arg_file = os.path.join(DIR_STR['ARGS_DIR'], script_name.replace('.py','.args'))
        arg_data = open(arg_file).read() if os.path.exists(arg_file) else ''

        # locate output and error, scrub prior results
        output_file = os.path.join(DIR_STR['OUTPUT_DIR'], script_name.replace('.py', '.out'))
        output_bad  = output_file + '.bad'
        err_file = os.path.join(DIR_STR['ERRORS_DIR'], script_name.replace('.py', '.err'))

        if os.path.exists(output_bad): os.unlink(output_bad)
        if os.path.exists(err_file):   os.unlink(err_file)

        # run test with redirected streams
        command = f'{sys.executable} {script_path} {arg_data}'
        test_run = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        test_run.stdin.write(input_data)
        test_run.stdin.close()
        
        test_output = test_run.stdout.read()         # read test stdout stream
        test_err    = test_run.stderr.read()         # read test stderr stream
        test_status = test_run.wait()                # get test exit code

        # analyze results
        if test_status:
            print("ERROR Status: %d for test %s" % (test_status, script_name))
        if test_err:
            print("Error stream:", err_file)
            open(err_file, 'wb').write(test_err)
        if test_status or test_err:
            open(output_bad, 'wb').write(test_output)
            num_fails += 1
        elif not os.path.exists(output_file) or args.force_gen:     # if first test or 
            print("Generating:", output_file)                       # override prev results
            open(output_file, 'wb').write(test_output)
        else:                                                       # if previous results exist
            prev_output = open(output_file, 'rb').read()            # compare with it
            if prev_output == test_output:
                print("Passed:", script_name)
            else:
                print("Failed output:", script_name, output_bad)
                open(output_bad, 'wb').write(test_output)
                num_fails += 1
    print('\n' + '*' * 35)
    print("Finished at", time.asctime())
    print("\nPassed:", len(scripts) - num_fails,
          "\nFailed:", num_fails,
          "\nTotal: ", len(scripts))
    if len(scripts):
        print("Pass Percent: %.3f%%" % 
              ((len(scripts)-num_fails) / len(scripts) * 100))
    else:
        print("No scripts found")

if __name__ == '__main__':
    main()

