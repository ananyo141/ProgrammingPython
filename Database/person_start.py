class Person:
    def __init__(self, name, age, pay = 0, job = None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job


if __name__ == '__main__':
    bob = Person('Bob Snugh', 42, 50000, 'Software')
    sue = Person('Sue Dearbon', 45, 40000, 'hardware')
    print(bob.name, sue.name, sep = ' and ')

    print(bob.name.split()[-1]) # print last name
    sue.pay *= 1.10
    print(sue.pay)
