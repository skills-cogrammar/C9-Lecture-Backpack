'''
Libary management system
'''

#Book object
class Book:
    def __init__ (self, author, title, genre):
        self.author = author
        self.title = title
        self.genre = genre
        self.is_available = True

# Library object
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        '''
        Method to add anew book to the library
        '''
        self.books.append(book)
        print(f"Added a new book: {book.title} by {book.author} by {book.genre}")

    def list_all_books(self):
        '''
        Method is supposed to iterate over the books list and display all books.
        '''
        for book in self.books:
            print(f"Title: {book.title}, Aythor: {book.author}, Genre: {book.genre}")