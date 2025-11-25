# 4. Менеджер ID
# Создай класс Item со статическим атрибутом last_id = 0.
#  Реализуй статический метод generate_id(),
# который увеличивает last_id на 1 и возвращает новое значение.
#  Используй метод для выдачи ID объектам другого класса при их создании
# Item

class Item:
    __last_id = 0

    @classmethod
    def generate_id(cls):
        cls.__last_id += 1
        return Item.__last_id

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = Item.generate_id()

    @classmethod
    def __str__(cls):
        return cls.__last_id


for i in range(100):
    item = Item(f"название {i}", 1000)
    print(item.name, item.id)

print(Item)

