# update the interactive database from the console
import shelve
from person import Person
fieldnames = ('name', 'age', 'job', 'pay')

with shelve.open('class-shelve.auto') as db:
    while True:
        key = input("\nKey? => ")
        if not key: break
        # if record already exists, update
        if key in db:
            record = db[key]
        else:
            record = Person(name = '?', age = '?')  # as python supports dynamic typing
        for field in fieldnames:
            currVal = getattr(record, field)        # get the current set attr value
            newVal = input(f"\t[{field}] = {currVal}\n\t\tnew?: ")
            setattr(record, field, newVal)          # set the new attribute value
                            
        db[key] = record       # save the record to database
            
