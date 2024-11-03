# # Ask student to create a list that contains their favourite movies
# favourite_movies = ["movie 1", "movie 2", "movie 3", "movie 4"]

# # Adding a new movie
# favourite_movies.append("movie 5")

# favourite_movies.insert(2, "Not A Movie")

# favourite_movies.remove("movie 4")
# print(favourite_movies)#
# print(favourite_movies.pop(1))

# print(favourite_movies[::3])

# # list -> 10 -> 11
# print(favourite_movies)# print(favourite_movies)#

# tuples
ids = (1, 2, 3, 5)

# tuple packing and unpacking
coordinates = (12.3434, 7.436823)  # packing

longitude, latitude = coordinates  # unpacking

# print("longitude: ", longitude)
# print("latitude: ", latitude)

# items = [1, 2, 3]


# def numbers(num):
#     while len(items) < num:
#         number = input("Enter a number: ")
#         items.append(number)
#     print(items)


# numbers(10)
# for item in items:
#     print(item * 10)

# Using sets to remove duplicates from list
# my_list = [1, 2, 2, 3, 4, 4, 5]
# unique_elements = list(set(my_list))
# print(unique_elements)  # Output: [1, 2, 3, 4, 5]


# dictionaries
person = {
    "name": "Bonaventure",
    "age": 22,
    "hobbies": ["hiking", "racing", "reading", "painting"]
}

person["occupation"] = "Software Engineer"
person["age"] = 23

# print(person)

# for key in person:
#     print(key)

user_profiles = [
    {
        "name": "Jake Doe",
        "email": "jakedoe@email.com"
    },
    {
        "name": "John Doe",
        "email": "jakedoe@email.com"
    },
    {
        "name": "Jude Doe",
        "email": "jakedoe@email.com"
    },
    {
        "name": "Joke Doe",
        "email": "jakedoe@email.com"
    },
    {
        "name": "Joe Doe",
        "email": "jakedoe@email.com"
    }
]

# del user_profiles[2]["name"]

# for user in user_profiles:
#     print(user["name"])

print(user_profiles)
print("*******************")
user_profiles.pop()
print(user_profiles)
