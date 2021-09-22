# Print the database of objects
import shelve

with shelve.open('class-shelve.auto') as db:
    for record in db:
        print(record, '=>\n', db[record])
