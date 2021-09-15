# Load the database from the pickle file, update (make changes) then save the changes
import pickle

dbfilename = 'people-pickle.auto'
# load the database from pickle
with open(dbfilename, 'rb') as dbfile:
    db = pickle.load(dbfile)

# make changes
db['sue']['pay'] *= 1.25    # give Sue 25% raise
db['bob']['job'] += ' and web-dev'  # add web dev to Bob's resume

# save the updated database
with open(dbfilename, 'wb') as dbfile:
    pickle.dump(db, dbfile)
