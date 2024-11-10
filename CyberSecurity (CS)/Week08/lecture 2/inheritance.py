# # Create class
# class Vehicle:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def start_engine(self):
#         return f"The engine of {self.brand} {self.model} is starting."

#     def stop_engine(self):
#         return f"The engine of {self.brand} {self.model} is stopping."

#     def fuel_type(self):
#         pass


# class Car(Vehicle):
#     def __init__(self, brand, model, year, seating_capacity):
#         super().__init__(brand, model, year)
#         self.seating_capacity = seating_capacity

#     def honk(self):
#         return "Car horn goes beep beep!"

#     def fuel_type(self):
#         return "Fuel type ABCD"


# class Truck(Vehicle):
#     def __init__(self, brand, model, year, cargo_capacity):
#         super().__init__(brand, model, year)
#         self.cargo_capacity = cargo_capacity

#     def load_cargo(self, weight):
#         if weight <= self.cargo_capacity:
#             return f"{weight} tons loaded onto the truck."
#         else:
#             return "Exceeds cargo capacity!"

# car = Car("Toyota", "Camry", 2020, 5)
# truck = Truck("Ford", "F-150", 2019, 3)

# print(car.start_engine())
# print(car.stop_engine())
# print(car.fuel_type())  # Calls overridden method in Car

# print(truck.start_engine())
# print(truck.load_cargo(2))
# print(truck.cargo_capacity)
# print(truck.fuel_type())  # Calls overridden method in Truck

# Method overriding
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


class Truck(Vehicle):
    def __init__(self, brand, model, year, cargo_capacity):
        super().__init__(brand, model, year)
        self.cargo_capacity = cargo_capacity

    def load_cargo(self, weight):
        if weight <= self.cargo_capacity:
            return f"{weight} tons loaded onto the truck."
        else:
            return "Exceeds cargo capacity!"

    def fuel_type(self):
        return "Diesel"

car = Car("Toyota", "Camry", 2020, 5)
truck = Truck("Ford", "F-150", 2019, 3)

print(car.fuel_type())  # Calls overridden method in Car

print(truck.fuel_type())  # Calls overridden method in Truck

# # super()
# class Person:

#     def __init__(self, name, surname, age, address):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.address = address

#     def walk(self):
#         print(f"{self.name} is walking!")

# class Student(Person):

#     def __init__(self, name, surname, age, address):
#         super().__init__(name, surname, age, address)
#         self.grades = []

#     def walk(self):
#         super().walk()
#         print(f"On their way to class!")


# # Polymorphism
# class Animal:

#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound

#     def make_sound(self):
#         print(f"{self} goes {self.sound}")

#     def walk(self):
#         print(f"The {type(self).__name__} goes for a walk!")
