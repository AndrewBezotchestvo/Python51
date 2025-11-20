from DZ8 import Weapon
# 2. Создать класс героя у которого будет атрибут - список оружия

# 3. Написать программу для взаимодействия с героем, напишите методы 
# для добавления нового оружия, удаления оружия из списка и просмотра всех орудий

class Hero:
    def __init__(self):
        self.__name = "Hero"
        self._rank = 3
        self.arsenal = []

    def add_new_weapon(self, weapon: Weapon):

        if weapon.name in self.arsenal:
            print(f"Оружие {weapon.name} уже есть в арсенале ")
        else:
            self.arsenal.append(weapon)
            print(f"Оружие {weapon.name} успешно добавлен в арсенал ")

    def show_weapon(self):
        
        if not self.arsenal:
            print(f"Арcенал пустой! ")
            return
        for weapon in self.arsenal:
            weapon.show_info()
            
    def del_weapon(self, name):
        if name in self.arsenal:
            self.arsenal.remove(name)
            print(f"Оружие {name} удалено из арсенала ")
        else:
            print(f"Оружие {name} нет в арсенале ")

def add_weapon(hero: Hero):
    new_weapon = Weapon(input("Введите названия оружия: "))
    hero.add_new_weapon(new_weapon)

def menu():
    ars = Hero()
    while True:
        print("1. Добавить оружие в арсенал ")
        print("2. Показать все оружие в арсенале ")
        print("3. Удалить оружие из арсенала ")
        print("4. Выйти ")
      
        vvod = input("Выбери действие: ")

        if vvod == '1':
            add_weapon(ars)
        
        if vvod == '2':
            ars.show_weapon()
        
        if vvod == '3':
            ars.del_weapon()
        
        if vvod == '4':
            break

menu()

