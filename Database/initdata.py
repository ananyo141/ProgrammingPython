# initialize data to be stored in files, pickles, shelves

# records
bob = {'name': 'Bob Smith',   'age': 42, 'pay': 30000, 'job': 'software-dev'}
sue = {'name': 'Sue Dearbon', 'age': 45, 'pay': 40000, 'job': 'hardware'    }
tom = {'name': 'Tom',         'age': 50, 'pay': 0,     'job':  None         }

# database to hold the records
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':  # when run as script
    for key in db:
        print(key, '=>\n  ', db[key])
