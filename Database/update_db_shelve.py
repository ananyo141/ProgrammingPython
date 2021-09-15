# Update the shelve version of the database
import shelve

shelveFilename = 'people-shelve.auto'

with shelve.open(shelveFilename) as shelveFile:
    sue = shelveFile['sue']     # retrieve sue then update the entry (shelve requires it)
    sue['pay'] *= 1.5           # give 50% raise
    shelveFile['sue'] = sue     
    shelveFile['rocky'] = {'name': 'Rocky Balboa', 'age': 50, 'pay': 60000, 'job': 'Action-hero'}
