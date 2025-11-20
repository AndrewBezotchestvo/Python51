# 1. Класс Weapon:
# С защищенными (protected) полями damage , reload , bullets, power 
# И приватным полем name 

# Напишите геттеры для damage reload power, name, bullets
# Напишите сеттер только для bullets

# 2. Создать класс героя у которого будет атрибут - список оружия

# 3. Написать программу для взаимодействия с героем, напишите методы 
# для добавления нового оружия, удаления оружия из списка и просмотра всех орудий

class Weapon:
    def __init__(self, name):
        self.__name = name
        self._damage = 100
        self._reload = 1
        self._bullets = 5
        self._power = 50
  
    @property
    def damage(self):
        return self._damage
    
    @property
    def reload(self):
        return self._reload
    
    @property
    def power(self):
        return self._power

    @property 
    def name(self):
        return self.__name
    
    @property 
    def bullets(self):
        return self._bullets
    @bullets.setter
    def bullets (self, new_bullets):
        self._bullets = new_bullets

    def show_info(self):
        print(self.__name, self._bullets, self._power, self.damage, sep="\n")


