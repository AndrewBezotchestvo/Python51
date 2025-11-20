# Задача 1: Умный вектор
#
# Создайте класс Vector, который представляет собой 2D-вектор с координатами x и y.
#
# Реализуйте методы:
#
# · init - инициализация
# · add - сложение векторов
# · sub - вычитание векторов
# · mul - умножение на число
# · str - красивое строковое представление
# · eq - сравнение векторов

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other):
        self.x *= other
        self.y *= other

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector x: {self.x}, y: {self.y}"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
print(v3)
v4 = v1 - v2
print(v4)
v1 * 10
print(v1)
print(v1 == v2)

