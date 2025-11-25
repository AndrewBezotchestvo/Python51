"""
1. Счётчик созданных объектов
Создай класс User, у которого есть
татический атрибут count, показывающий,
сколько объектов этого класса было создано.
 Каждый раз при создании нового объекта
 увеличивай счётчик.
 Добавь статический метод get_count(),
 возвращающий текущее значение счётчика.
"""
class User:
    __count = 0
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        User.__count += 1

    @staticmethod
    def get_count():
        return User.__count

for _ in range(100):
    User("name")
print(User.get_count())
