# interact script
import shelve
fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(field) for field in fieldnames)  # get the maximum number of characters in the field

with shelve.open('class-shelve.auto') as db:
    while True:
        key = input("Input Key: ").lower()
        if not key: break   # break if user inputs nothing
        try:
            record = db[key]
        except KeyError:
            print(key, "doesn't exist!")
        else:
            for field in fieldnames:
                print(field.ljust(maxfield), '=> ', getattr(record, field))    # print the attribute of the object

