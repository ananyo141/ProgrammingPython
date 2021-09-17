class Person:
    """
    A general person, data and logic
    """
    def __init__(self, name, age, pay = 0, job = None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    def getLastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1 + percent)
    def __str__(self):
        return f'{self.__class__.__name__} => {self.name}: {self.job}, {self.pay}'

class Manager(Person):
    """
    A person with custom raise
    inherits general lastName, str and add methods
    """
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'Manager')
    def giveRaise(self, percent, bonus = 0.1):
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith', 35)
    sue = Person('Sue Dearbon', 47, 30000, 'software')
    tom = Manager(name = 'Tom Baggins', age = 50, pay = 60000)

    db = [bob, sue, tom]
    print(sue, sue.pay, sue.getLastName())
    for obj in db:
        obj.giveRaise(0.10) # raise every object instance
        print(obj)  # common str method (operator overload)
