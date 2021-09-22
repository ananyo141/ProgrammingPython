# Read the database saved in the pickle format
import pickle

dbfilename = 'people-pickle.auto'
with open(dbfilename, 'rb') as dbfile:
    db = pickle.load(dbfile)

# print the record to the screen
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])
