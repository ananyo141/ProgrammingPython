# Dump the contents of the database in the shelve file
import shelve

shelveFilename = 'people-shelve.auto'
with shelve.open(shelveFilename) as shelveFile:
    for key in shelveFile:
        print(key, '=>\n ', shelveFile[key])
    print(shelveFile['sue']['name'])
