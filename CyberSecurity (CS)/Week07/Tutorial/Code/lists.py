str_list = ["This", "is", "a", "list", "of", "strings"]
int_list = [1, 2, 3, 4, 5]
float_list = [1.2, 2.4, 3.0, 2.5, 2.1]
mixed_list = [1, "Hello", True, 3.4]

# Ask student to create a list that contains their favourite movies
favourite_movies = ["movie 1", "movie 2", "movie 3", "movie 4"]

# Adding a new movie
favourite_movies.append("movie 5")

favourite_movies.insert(2, "movie 6")

# Removing values
favourite_movies.pop(2)

favourite_movies.remove("movie 6")

# Changing values
favourite_movies[0] = "movie 10"

# Some common methods
favourite_movies.reverse()

favourite_movies.sort()

favourite_movies.extend(["movie 7", "movie 8", "movie 9"])

favourite_movies.count()

# Loops and lists
for movie in favourite_movies:
    print(movie)

for i in range(len(favourite_movies)):
    print(favourite_movies[i])