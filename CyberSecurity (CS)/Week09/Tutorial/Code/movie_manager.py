from random import randint
from movie import Movie

def add_movie(movies_list, title, rating, review):
    if search_movie(movies_list, title):
        print("Movie already exists")
        return
    movies_list.append(Movie(title, review, rating))
    print(f"Movie {title} added to list.")


def update_movie(movies_list, title, rating, review):
    for movie in movies_list:
        if title == movie.title:
            if review:
                movie.update_review(review)
                print(f"Review for {title} updated.")
            if rating:
                movie.update_rating(rating)
                print(f"Rating for {title} updated to {rating}/10.")
            return
    print(f"Movie {title} not found!")

def search_movie(movie_list, movie_title):
    for movie in movie_list:
        if movie_title == movie.title:
            return movie
        else:
            print(f"Movie {title} not found!")

def display_movies(movies_list, sorted_by_rating=True):
    if not movies_list:
        print("No  movies in list!")
        return
    
    print("Movie Collection")
    if sorted_by_rating:
        movies_list.sort(key=lambda x: x.rating, reverse=True)

    for i, movie in enumerate(movies_list, 1):
        print(f"{i}. {movie.title} - Rating: {movie.rating}/10")

def remove_movie(movies_list, title):
    movie = search_movie(movies_list, title)
    if movie:
        movies_list.remove(movie)
        print(f"Movie {title} removed!")
    else:
        print(f"Movie {title} not found!")


def random_movie(movies_list):
    if movies_list:
        index = randint(0, len(movies_list)-1)
        return movies_list[index]


def save_movies(movies_list):
    with open("movies.txt", "w") as file:
        for movie in movies_list:
            file.write(f"{movie.title}|{movie.rating}|{movie.review}\n")


def retrieve_movies():
    movies_list = []
    try:
        with open("movies.txt", "r") as file:
            for line in file.readlines():
                line = line.strip().split("|")
                movies_list.append(Movie(line[0], line[2], float(line[1])))
    except FileNotFoundError:
        with open("movies.txt", "w") as file:
            pass
    return movies_list


MAIN_MENU = """Choose an option:
1. Add Movie
2. Update Movie Review or Rating
3. Search for a Movie
4. Display All Movies (Sorted by Ratings)
5. Remove a Movie
6. Recommend Movie
\n0. Exit
:"""

movies = retrieve_movies()

while True:  
    choice = input(MAIN_MENU)
    
    if choice == "1":
        title = input("Please enter the title: ")
        rating = float(input("Please enter the rating: "))
        review = input("Please enter the review:\n")
        add_movie(movies, title, rating, review)
        save_movies(movies)
    elif choice == "2":
        title = input("Please enter the title to update: ")
        rating = input("Please enter new rating(Leave Blank for no change): ")
        rating = float(rating) if rating else None
        review = input("Please enter new review(Leave Blank for no change):\n")
        update_movie(movies, title, rating, review)
        save_movies(movies)
    elif choice == "3":
        title = input("Enter the title of the movie to search: ")
        movie = search_movie(movies, title)
        if movie:
            print("-"*80)
            print(movie)
            print("-"*80)
    elif choice == "4":
        display_movies(movies, sorted_by_rating=True)
    elif choice == "5":
        title = input("Enter the title of the movie to remove: ")
        remove_movie(movies, title)
        save_movies(movies)
    elif choice == "6":
        movie = random_movie(movies)
        if movie:
            print("Movie to watch:")
            print(movie)
        else:
            print("No movies in collection!")
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
