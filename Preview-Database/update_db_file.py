# Update the db file
from make_db_file import loadDbase, storeDbase
db = loadDbase()
db['sue']['pay'] *= 1.10    # give sue 10% raise
db['tom']['name'] = 'Tom Tom'
storeDbase(db)
