# make the OO database persistent
import shelve
from person import Person
from manager import Manager

bob = Person('Bob Smith', 60, 30000, 'software')
sue = Person('Sue Dearbon', 26, 40000, 'hardware')
tom = Manager('Tom Hanks', 62, 60000)

with shelve.open('class-shelve.auto') as db:
    db['bob'] = bob
    db['sue'] = sue
    db['tom'] = tom

    
