class Predator:
    def __init__(self, area, age, weight, height, food):
        self.age = age
        self.area = area
        self.weight = weight
        self.height = height
        self.food = food
    def hunt(self):
        print("охота")

class Tiger(Predator):
    def __init__(self, area, age, weight, height, food):
        super().__init__(area, age, weight, height, food)

class Lion(Predator):
    def __init__(self, area, age, weight, height, food):
        super().__init__(area, age, weight, height, food)