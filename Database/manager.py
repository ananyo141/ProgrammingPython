from person import Person

class Manager(Person): # inherit from the Person class
    
    def __init__(self, name, age, pay):
        super().__init__(name, age, pay, 'Manager')

    def giveRaise(self, percent, bonus = 0.1):
        Person.giveRaise(self, percent + bonus) # managers get an additional 10% bonus with raise


if __name__ == '__main__':
    tom = Manager(name = 'Tom Argus', age = 63, pay = 50000)
    print(tom.getLastName(), tom.pay)
    tom.giveRaise(0.4) # 40 percent raise
    tom + 0.5
    print(tom.pay)
    print(tom.job)
    print(tom)
