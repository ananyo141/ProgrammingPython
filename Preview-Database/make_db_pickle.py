# Use the pickle module to save the database efficiently
from initdata import db
import pickle

dbfilename = 'people-pickle.auto'
with open(dbfilename, 'wb') as dbfile:
    pickle.dump(db, dbfile)     # dump the database object db into the opened stream
