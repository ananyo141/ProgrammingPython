# Update the database
import shelve
from person import Person

with shelve.open('class-shelve.auto') as db:
    tom = db['tom']
    tom + 0.5 
    bob = db['bob']
    bob.pay = 40000
  
    db['tom'] = tom   
    db['bob'] = bob
    db['harry'] = Person('Harry Sawant', 22, 25000) # create a new object
