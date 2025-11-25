class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'Счет {self.name} - {self.balance} руб.'

    def __add__(self, account: int):
        self.balance += account
        return f'Баланс: {self.balance}'

    def add(self, account = 50):
        self.balance += account
        return f'Баланс: {self.balance}'

    def __eq__(self, other):
        return self.balance == other.balance

class Person:
    defoult_name = "defoult"
    def __init__(self, name):
        self.name = name

print(Person.defoult_name)
tom = Person("tom")
print(tom.defoult_name)
Person.defoult_name = "defoult2"
print(Person.defoult_name)
tom.defoult_name = "defoult3"
print(Person.defoult_name)
print(tom.defoult_name)

tom.age = 100
print(tom.age)

