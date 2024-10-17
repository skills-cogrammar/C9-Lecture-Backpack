# Creating dictionaries

# We can create an empty dictionary
my_dict = {}

# Or we could populate it.
my_dict = {'name': 'James',       # Show student how to use multiple lines for declaration
           'surname': 'Peterson'}

# We can use the dict() functions as well
my_dict = dict(name='James', surname='Peterson')

# We can use more than just strings in our dictionaries
num_dict = {1: 'One', 2: 'Two', 3: 'Three'}
num_dict = {1: 2, 2: 3, 3:4}

int_float = {1: 1.0, 2: 2.0, 3: 3.0}
float_int = {1.0: 1, 2.0: 2, 3.0: 3}

bool_dict = {'yes': True, 'no': False}

list_dict = {'scores': [7, 8, 6, 7, 7, 8, 9],
             'players': ['Jesse', 'Mark']}

students = {'Dave': {"surname": "Wheeler", "age": 27},
            "Nina": {"surname": "Jackson", "age": 26},
            "Victoria": {"surname": "Tomson", "age": 30}}


# Student challenge
# Create a dictionary named my_pet with the following data
# type = "Dog"
# breed = "Labrador"
# furr_color = "Brown"
# age = 6
# weight = 30.2
# vacinated = True
my_pet = {'type': 'Dog',
          'breed': 'Labrador',
          'furr_color': 'Brown',
          'age' : 6,
          'weight': 30.2,
          'vacinated': True}

my_pet = dict(type='Dog', breed='Labrador', furr_color='Brown',
              age=6, weight=30.2, vacinated=True)

my_pet = dict((('type','Dog'), ('breed', 'Labrador'), ('furr_color', 'Brown'),
              ('age', 6), ('weight', 30.2), ('vacinated', True)))


# Retrieving values
personal_details = {'name': 'John',
                    'surname': 'Cena',
                    'age': 50,
                    'height': 188.4}

print(personal_details['name'])
print(personal_details['height'])
# Student challenge
# How can I retrieve the age from our dictionary.
print(personal_details['age'])


# Adding Values
computer = {}

computer["CPU"] = "Ryzen 5 5600"
computer["PSU"] = "600W"
# Student Challenge
# Add some RAM to our computer dictionary.
computer["RAM"] = "16GB"

# We can use the update() methods as well
computer.update(GPU="Geforce RTX 4060")
computer.update(Case="Corsair 6500 Series")
# Alternative
computer.update(GPU="Geforce RTX 4060", Case="Corsair 6500 Series")

# Student Challenge
# Add a SSD to the computer dictionary using the update() methods
computer.update(SSD="1TB")


# Removing Values
scores = {"Peter": 80, "Sahra": 82, "Jake": 77, "Tina": 79, "Ben": 73}
print(scores)

del scores["Jake"]
print(scores)

del scores["Tina"]
print(scores)

# Student Challenge
# How can we delete Peter's score?
del scores['Peter']

# We can use the pop() methods to also remove values
inventory = {'bread': 10,
             'milk': 8,
             'eggs': 90,
             'sugar': 4}

inventory.pop('milk')
print(inventory)
eggs = inventory.pop('eggs')
print(inventory)

# Student challenge
# Write the code to remove the sugar using .pop()
inventory.pop('sugar')


# Dictionary Methods
city_populations = {
    "New York": 8.4,
    "Tokyo": 37.4,
    "Paris": 2.1,
    "Delhi": 31.0
}

print(city_populations.get("Tokyo"))
print(city_populations.get("Paris"))
print(city_populations.get("London", "Unknown"))

# Student challenge
# Write the code to retrieve the population of Delhi from the dictionary
print(city_populations.get("Delhi"))


print(city_populations.keys())
print(city_populations.values())
print(city_populations.items())

london = city_populations.setdefault("London", 8.9)
print(city_populations)
print(london)
paris = city_populations.setdefault("Paris", 3)
print(city_populations)
print(paris)

# Student cahllenge
# How can I determine the length of a dictionary?
# Hint: how do I get the length of a string?
print(len(city_populations))


# Looping over Dictionaries
animals = {"Lions": 5, "Tigers": 7, "Cheetahs": 3, "Bears": 2, "Wild Dogs": 6}

for animal in animals:
    print(animal)
# Student challenge
# Which dictionary method can I use here to get the same result?
for animal in animals.keys():
    print(animal)

for amount in animals.values():
    print(amount)

for animal, amount in animals.items():
    print(f"{animal} - {amount}")

# Student challenge
# Create a loop that will calculate the total amount of animals in the park
total = 0
for amount in animals.values():
    total += amount
print(f"Total amount of animals in park: {total}")


# Copying Dictionaries
scores = {"Peter": 80, "Sahra": 82, "Jake": 77, "Tina": 79, "Ben": 73}
scores_copy = scores

scores_copy.pop("Peter")

print(scores)
print(scores_copy)
# Why was peter removed from the original scores?

scores_copy = scores.copy()

# Deepcopy
students = {'Dave': {"surname": "Wheeler", "age": 27},
            "Nina": {"surname": "Jackson", "age": 26},
            "Victoria": {"surname": "Tomson", "age": 30}}

new_students = students.copy()
new_students['Dave'] = None
print(students)
print(new_students)

new_students['Nina']['surname'] = 'Peters'
print(students)
print(new_students)

from copy import deepcopy
new_students = deepcopy(students)

new_students['Nina']['surname'] = 'Peters'
print(students)
print(new_students)