 # Приватный инвентарьВ классе Character
 # создай приватный список __inventory.
 # Добавь методы:
 #    add_item(item)show_inventory()
 # Сделай так, чтобы к __inventory
 # нельзя было обратиться напрямую.

class Character:
    def __init__(self, name):
        self.__name = name
        self.__inventory = []

    def add_item(self, item):
        self.__inventory.append(item)

    def show_inventory(self):
        for item in self.__inventory:
            print(item)

    @property
    def inventory(self):
        return self.__inventory

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if new_name.isalpha() and len(new_name) > 1 and len(new_name) <= 30:
            self.__name = new_name
        else:
            print("имя не корректно")

hero = Character("Иван")
hero.add_item("Молот")
hero.show_inventory()
print(hero.inventory)
print(hero.name)
hero.name = "Ян"
print(hero.name)


