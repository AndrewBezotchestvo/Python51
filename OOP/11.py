class Inventory:
    def __init__(self, capacity=10):
        self.__capacity = capacity
        self.__items = {}

        self.__gold = 0

    # 1. Добавление предметов через +
    def __add__(self, other):
        """Добавить предмет: inventory + ('sword', 1)"""
        if len(self.__items) >= self.__capacity:
            print("Инвентарь полон")
            return
        if other[0] in self.__items.keys():
            self.__items[other[0]] += other[1]
        else:
            self.__items[other[0]] = other[1]

    # 2. Удаление предметов через -
    def __sub__(self, other):
        """Удалить предмет: inventory - 'sword'"""
        if self.__items.__contains__(other):
            self.__items[other] -= 1
            if self.__items[other] == 0:
                self.__items.pop(other)
    # 3. Умножение для дублирования предметов
#    def __mul__(self, count):
#         """Увеличить количество предмета: inventory * 2"""
#         pass

    # 4. Проверка наличия через in
    def __contains__(self, item_name):
        """Проверка: 'sword' in inventory"""
        if item_name in self.__items.keys():
            print("данный предмет есть в инвентаре")
            return True
        else:
            print("данного предмета есть в инвентаре")
            return True

    # 5. Получение количества через []
    def __getitem__(self, item_name):
        """Получить количество: inventory['sword']"""
        if item_name in self.__items.keys():
            return self.__items[item_name]

    # 6. Красивый вывод
    def __str__(self):
        """Вывод инвентаря"""
        answer = f"Баланс {self.__gold} \nИнвентарь:\n"

        for key, value in self.__items.items():
            answer += f"{key}: {value}\n"
        answer += f"Заполненость: {len(self.__items)}/{self.__capacity}"

        return answer

    # 7. Сравнение инвентарей
    def __eq__(self, other):
        isSame = True

        isSame = self.__gold == other.__gold
        isSame = self.__items == other.__items and isSame
        isSame = self.__capacity == other.__capacity and isSame

        return isSame
        # 8. Сложение инвентарей

    def __mul__(self, other):
        for key, value in self.__items.items():
            if key not in self.__items.keys() and len(self.__items) >= self.__capacity:
                continue
            self.__items[key] += value


inv1 = Inventory(10)
inv2 = Inventory()

inv1 + ("posion", 3)
inv1 + ("sword", 15)
inv1 + ("brush", 15)

print(inv1)
inv1 - "posion"
print(inv1)
"sword" in inv1
print(inv1["brush"])

print(inv1 == inv2)
inv2 + ("posion", 5)
inv1 * inv2
print(inv1)