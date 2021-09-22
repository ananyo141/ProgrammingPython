# Make database using shelve module
import shelve
from initdata import db

shelveFileName = 'people-shelve.auto'

with shelve.open(shelveFileName) as shelveDb:
    for rec in db:
        shelveDb[rec] = db[rec]

