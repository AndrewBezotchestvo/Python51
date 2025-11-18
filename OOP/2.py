class Person:

    def __init__(self, name):
        self.name = name
        print("Создан человек с именем", self.name)

    def __del__(self):
        print("Удален человек с именем", self.name)


def create_person():
    tom = Person("Tom")


create_person()
print("Конец программы")