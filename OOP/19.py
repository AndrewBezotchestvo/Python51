class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def show_info(self):
        print(self.brand, self.model, self.year)

class OffRoadCar(Car):
    def __init__(self, brand, model, year, engine_volume):
        super().__init__(brand, model, year)
        #Car.__init__(self, brand, model, year)
        self.engine_volume = engine_volume
    def show_targets(self):
        print("езда по бездорожью")
    def show_info(self):
        super().show_info()
        print(f"Объем двигателя: {self.engine_volume} литров")
    def road(self):
        print("Поехал по дюнам")

class SportCar(Car):
    def __init__(self, brand, model, year, max_speed):
        super().__init__(brand, model, year)
        self.max_speed = max_speed
    def show_targets(self):
        print("езда по треку")
    def show_info(self):
        super().show_info()
        print(f"Максимальная скорость: {self.max_speed} км/ч")
    def road(self):
        print("Поехал по треку")

class FamilyCar(Car):
    def __init__(self, brand, model, year, seats):
        super().__init__(brand, model, year)
        self.seats = seats
    def show_targets(self):
        print("езда по треку")
    def show_info(self):
        super().show_info()
        print(f"Вместимость: {self.seats} человек")
    def road(self):
        print("Поехал по городу")


car1 = Car("BMW", "M5", 2025)
car2 = OffRoadCar("Toyota", "Land Cruiser", 2000, 5)
car3 = SportCar("Porche", "911 GT3", 2000, 5)
car4 = FamilyCar("Toyota", "StepWGN", 2000, 5)

for car in [car2, car3, car4]:
    print("Меню \n "
          "1. информация о автомобиле \n"
          "2. цель автомобиля")
    if isinstance(car, OffRoadCar):
        print("3. Поездить по дюнам")
    elif isinstance(car, SportCar):
        print("3. Поездить по треку")
    elif isinstance(car, FamilyCar):
        print("3. Поездить по городу")

    action = input("Выберете действие: ")

    match action:
        case "1":
            car.show_info()
        case "2":
            car.show_targets()
        case "3":
            car.road()
        case _:
            print("не верное действие")



#isinstance(car2, OffRoadCar) - проверка относиться ли объект
# к конкретному классу

#добавить еще 2 дочерних класса и реализовать систему
# меню для разных вариантов автомобиля, к примеру
#если автомобиль является объектом класса OffRoadCar
#в меню вы должны отобразить все возможные действия с offroadCar