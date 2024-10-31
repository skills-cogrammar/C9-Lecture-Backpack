my_dict = {"name": "Peter", 
           "surname": "Parker"}


my_dict = dict(name="Peter", 
               surname="Parker")

num_dict = {1: "one",
            2: "two",
            3: "three"}
num_dict = {1: 2,
            2: 3,
            3: 4}

bool_dict = {"yes": True,
             "no": False}

list_dict = {"scores": [4, 5, 7, 8, 6, 4],
             "players": ["James", "parker"]}

students = {"Dave": {'surname': "Wheeler", "age":22}}

# Accessing Values
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict['name'])  # Output: 'Alice'

# Using the get() method (avoids error if the key is missing)
print(my_dict.get('age'))  # Output: 25
print(my_dict.get('country', 'USA'))  # Output: 'USA' (default if 'country' is not found)


# Adding and updating values
my_dict = {'name': 'Alice', 'age': 25}
my_dict['city'] = 'New York'  # Adding a new key-value pair
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

my_dict['age'] = 26  # Updating an existing key
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# Removing Values
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Using pop() method
age = my_dict.pop('age')
print(age)       # Output: 25
print(my_dict)   # Output: {'name': 'Alice', 'city': 'New York'}

# Using del statement
del my_dict['city']
print(my_dict)   # Output: {'name': 'Alice'}

# Using popitem() - removes and returns the last key-value pair
my_dict = {'name': 'Alice', 'age': 25}
item = my_dict.popitem()
print(item)      # Output: ('age', 25)
print(my_dict)   # Output: {'name': 'Alice'}


# Looping Dictionaries
my_dict = {'name': 'Alice', 'age': 25}
for key in my_dict:
    print(key)  # Output: 'name', 'age'

for value in my_dict.values():
    print(value)  # Output: 'Alice', 25

for key, value in my_dict.items():
    print(f"{key}: {value}")  # Output: name: Alice, age: 25
