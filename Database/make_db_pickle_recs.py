# Make individual pickle files for each record in database
import pickle
from initdata import db

for record in db:
    with open(record + '.pkl', 'wb') as recfile:
        pickle.dump(db[record], recfile)
