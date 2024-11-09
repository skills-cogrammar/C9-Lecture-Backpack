class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def walk(self):
        print("I'm taking a walk!")

    def read(self):
        print("I'm reading a book!")


my_person = Person("Dan", 23, "Lawyer")

print(my_person.name)
my_person.walk()
my_person.read()
