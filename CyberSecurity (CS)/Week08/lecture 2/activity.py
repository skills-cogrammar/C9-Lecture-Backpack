# Base class (Parent class)
class Animal:
    def __init__(self, mouth, legs, eyes, sound):
        self.mouth = mouth
        self.legs = legs
        self.eyes = eyes
        self.sound = sound

    def speak(self):
        pass

# Derived class
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"

class Cat(Animal):
    def __init__(self, mouth, legs, eyes, speak):
        super().__init__(mouth, legs, eyes, speak)

    def speak()
        print('Meaow')

# my_dog = Dog("Buddy")

# print(my_dog.speak())
