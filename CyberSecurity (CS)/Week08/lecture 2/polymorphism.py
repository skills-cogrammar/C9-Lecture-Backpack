class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return f"The engine of {self.brand} {self.model} is starting."

    def stop_engine(self):
        return f"The engine of {self.brand} {self.model} is stopping."

    def fuel_type(self):
        return "Generic Fuel"


class Car(Vehicle):
    def __init__(self, brand, model, year, seating_capacity):
        super().__init__(brand, model, year)
        self.seating_capacity = seating_capacity

    def honk(self):
        return "Car horn goes beep beep!"

    def fuel_type(self):
        return "Petrol or Electric"

vehicle = Vehicle("Toyota", "Camry", 2020)
car = Car("Toyota", "Camry", 2020, 5)

def fuel_type(vehicle):
    print(vehicle.fuel_type())

fuel_type(car)
