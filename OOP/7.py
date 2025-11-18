# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя,
# объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных,
# реализуйте доступ к отдельным полям через методы класса.



class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_name(self):
        return self.name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 18:
            self.__age = age
        else:
            print("вы не совершенно летний")

    def set_name(self, new_name):
        self.name = new_name

human = Person("Vasia", 23)
print(human.age)
human.age = 100
print(human.age)