# Fetch a single record pickle and update and save changes
import pickle, sys

filename = input("File to change: ")
# open the record file 
try:
    with open(filename, 'rb') as recPickle:
        record = pickle.load(recPickle)
except FileNotFoundError:
    sys.exit("Pickle file not found in cwd.")
except IOError:
    sys.exit("Input Output error")
except OSError:
    sys.exit("Unable to open file, check filename for explicit characters")

# increase pay by 10%
record['pay'] *= 1.10

# save the file
with open(filename, 'wb') as recPickle:
    pickle.dump(record, recPickle)
