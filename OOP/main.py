class Person:

    def __init__(self, name, age):
        self.name = name  # имя человека
        self.age = age  # возраст человека


tom = Person("Tom", 22)

tom.company = "Microsoft"
print(tom.company)  # Microsoft