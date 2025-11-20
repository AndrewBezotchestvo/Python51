class Spell:
    def __init__(self, name, cost, damage, level):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.level = level

    def __eq__(self, other):
        return (self.name == other.name and
                self.cost == other.cost and
                self.damage == other.damage and
                self.level == other.level)

class Spellbook:
    def __init__(self, max_mana=100):
        self.max_mana = max_mana
        self.current_mana = max_mana
        self.spells = []

    # 1. Добавление заклинания через +
    def __add__(self, other):
        new_spell = Spell(other[0], other[1], other[2], other[3])
        for spell in self.spells:
            if spell == new_spell:
                print("Такое заклинанание существует")
                return
        self.spells.append(new_spell)
        print("Заклинанание добавленно")

    # 2. Каст заклинания через -
    def __sub__(self, spell_name):
        for spell in self.spells:
            if spell.name == spell_name:
                self.current_mana -= spell.cost
                print(f"преминено заклинание {spell_name}, "
                      f"отнялось манны {spell.cost}")

    # 4. Проверка доступности заклинания через in
    def __contains__(self, spell_name):
        for spell in self.spells:
            if spell.name == spell_name:
                return True
        return False

    # 5. Получение информации о заклинании через []
    def __getitem__(self, spell_name):
        """Получить информацию: spellbook['fireball']"""
        for spell in self.spells:
            if spell.name == spell_name:
                return (f"Название {spell.name}\n "
                        f"Стоимость {spell.cost}\n"
                         f"Урон {spell.damage}\n"
                         f"Уровень {spell.level}\n")
        return "Данного заклинания нету"


    # 8. Красивый вывод
    def __str__(self):
        answer = f"Количество манны {self.current_mana} \nЗаклинания:\n"

        for spell in self.spells:
            answer +=  (f"Название: {spell.name} "
                        f"Стоимость: {spell.cost} "
                         f"Урон: {spell.damage} "
                         f"Уровень: {spell.level} \n")

        return answer

    # 9. Длина - количество известных заклинаний
    def __len__(self):
        return len(self.spells)


spellbook = Spellbook()
spellbook + ("Fireboll", 30, 30, 1)
spellbook + ("Fireboll", 30, 30, 1)
spellbook + ("Fireboll", 40, 60, 2)
print(spellbook)
spellbook -= "Fireboll"
print("fire" in spellbook)

print(spellbook["Fireboll"])