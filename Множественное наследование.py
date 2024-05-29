class Vehicle:
    vehicle_type = "none"


class Car(Vehicle):
    price = 1000000

    def horse_powers(self):
        return 180


class Nissan(Car, Vehicle):
    def __init__(self):
        super().__init__()
        self.vehicle_type = "Авто"
        self.price = 1400000

    def horse_powers(self):
        return 230


nissan_car = Nissan()
print(f'Vehicle type: {nissan_car.vehicle_type}')
print(f'Car price: {nissan_car.price}')
print(f'Horse powers of car: {nissan_car.horse_powers()}')