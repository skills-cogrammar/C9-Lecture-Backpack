class Dog:
    species = "Canis Lupus"

    def __init__(self, name, age):
        self.__name = name # private
        self._age = age # protected

    def greet(self):
        return f"Hi {self.species}"

    def get_name(self):
        return self.__name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        self._age = new_age

my_dog = Dog("Jimmy", 5)
your_dog = Dog("Jugg", 3)
my_dog.set_age(10)
print(my_dog.get_age())

# define a class for a person
