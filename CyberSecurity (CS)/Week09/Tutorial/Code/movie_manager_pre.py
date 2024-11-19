from movie import Movie
from random import randint

def add_movie(movie_list, title, review, rating):
    """Adds a new movie to the collection."""
    for movie in movie_list:
        if movie.title == title:
            print("Movie already added!")
            return
    movie_list.append(Movie(title, review, rating))
    print(f"Movie '{title}' added with rating {rating}/10.")


def update_movie(movie_list, title, review=None, rating=None):
    """Updates the review or rating of an existing movie."""
    for movie in movie_list:
        if title == movie.title:
            if review:
                movie.update_review(review)
                print(f"Review for '{title}' updated.")
            if rating:
                movie.update_rating(rating)
                print(f"Rating for '{title}' updated to {rating}/10.")
            return
    else:
        print(f"Movie '{title}' not found.")


def search_movie(movie_list, title):
    """Searches for a movie by title and displays its details."""
    for movie in movie_list:
        if title == movie.title:
            print(f"\nMovie Found: {title}")
            print(f"Review: {movie.review}")
            print(f"Rating: {movie.rating}/10")
        else:
            print(f"Movie '{title}' not found.")


def display_movies(movie_list, sorted_by_rating=False):
    """Displays all movies, optionally sorted by their ratings."""
    if not movie_list:
        print("No movies in the collection.")
        return

    print("\nMovie Collection:")
    if sorted_by_rating:
        movie_list.sort(key=lambda x: x.rating, reverse=True)

    for i, movie in enumerate(movies, 1):
        print(f"{i}. {movie.title} - Rating: {movie.rating}/10 - Review: {movie.review}")


def remove_movie(movie_list, title):
    """Removes a movie from the collection."""
    for movie in movie_list:
        if title == movie.title:
            index = movie_list.index(movie)
            del movie_list[index]
            print(f"Movie '{title}' removed.")
        else:
            print(f"Movie '{title}' not found.")


def random_movie():
    """Selects and returns a random movie from the movie list"""
    if movies:
        index = randint(0, len(movies)-1)
        return movies[index]
    

def save_movies(movie_list):
    """Save all movies in movie list to a text file."""
    with open("movies.txt", "w") as file:
        for movie in movie_list:
            file.write(f"{movie.title}|{movie.rating}|{movie.review}\n")


def retrieve_movies():
    """Retrieve all movie data from movie text file."""
    movie_list = []
    try:
        with open("movies.txt", "r") as file:
            for line in file.readlines():
                line = line.strip().split("|")
                movie_list.append(Movie(line[0], line[2], float(line[1])))
    except FileNotFoundError:
        with open("movies.txt", "w") as file:
            pass
    return movie_list


movies = retrieve_movies()
while True:
    print("\nChoose an option:")
    print("1. Add Movie")
    print("2. Update Movie Review or Rating")
    print("3. Search for a Movie")
    print("4. Display All Movies (Sorted by Ratings)")
    print("5. Remove a Movie")
    print("6. Recommend Movie")
    print("\n0. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        title = input("Enter the movie title: ")
        review = input("Enter your review: ")
        rating = float(input("Enter your rating (0-10): "))
        add_movie(title, review, rating)
        save_movies(movies)
    elif choice == "2":
        title = input("Enter the movie title to update: ")
        review = input("Enter the new review (leave blank to keep current): ") or None
        rating = input("Enter the new rating (leave blank to keep current): ")
        rating = float(rating) if rating else None
        update_movie(title, review, rating)
        save_movies(movies)
    elif choice == "3":
        title = input("Enter the movie title to search: ")
        search_movie(title)
    elif choice == "4":
        display_movies(sorted_by_rating=True)
    elif choice == "5":
        title = input("Enter the movie title to remove: ")
        remove_movie(title)
        save_movies(movies)
    elif choice == "6":
        movie = random_movie()
        if movie:
            print("Movie to watch:")
            print(movie)
        else:
            print("No movies in the collection.")
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
