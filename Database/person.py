class Person:
    def __init__(self, name, age, pay = 0, job = None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def getLastName(self) -> str:
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    # operator overloading
    def __str__(self): # for str() conversions  
        stringRepresentation = self.__class__.__name__ + ' Class'
        for key, value in self.__dict__.items():
            stringRepresentation += f'\n{key.title()}: {value}'
        return stringRepresentation
    
    def __add__(self, percent): # for adding (+)
        self.giveRaise(percent)


if __name__ == '__main__':
    bob = Person('Bob Smith', 32, 40000, 'hardware')
    sue = Person('Sue Dearbon', 26, 20000, 'web-dev')
    print(bob.name, sue.pay)

    print(bob.getLastName())
    sue.giveRaise(0.40)
    print(sue.pay)
