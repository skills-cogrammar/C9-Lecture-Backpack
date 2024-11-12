# Base class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Some generic animal sound."

    def move(self):
        return "Animal moves around."

    def __str__(self):
        return f"{self.name} (Age: {self.age})"


# Subclass: Dog
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball!"

    def __str__(self):
        return f"{self.name}, a {self.breed} (Age: {self.age})"


# Subclass: Cat
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        return "Meow!"

    def scratch(self):
        return f"{self.name} is scratching the furniture."

    def __str__(self):
        return f"{self.name}, a {self.color} cat (Age: {self.age})"


# Subclass: Bird
class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def make_sound(self):
        return "Chirp!"

    def fly(self):
        return f"{self.name} is flying high!"

    def __str__(self):
        return f"{self.name}, a {self.species} (Age: {self.age})"


# Example usage
dog = Dog("Buddy", 5, "Golden Retriever")
cat = Cat("Whiskers", 3, "tabby")
bird = Bird("Tweety", 2, "canary")

print(dog)
print(dog.make_sound())
print(dog.fetch())

print(cat)
print(cat.make_sound())
print(cat.scratch())

print(bird)
print(bird.make_sound())
print(bird.fly())
