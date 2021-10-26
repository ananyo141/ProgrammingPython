# A recursive function for stand-in replacement of os.walk() 

import sys, os

def mylister(directory):
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            mylister(path)
        else:
            print(path)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        mylister(sys.argv[1])
    else:
        print("No arguments")
