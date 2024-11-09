"""
define a class for a Library and define a method for borrowing a book
"""

# class Book:
#     def __init__(self, title, author, genre, available):
#         self.title = title
#         self.author = author
#         self.genre = genre
#         self.available = True

# class Library:
#     def __init__(self):
#         self.books = []
#         self.members = []

#     def add_book(self):
#         pass


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_available = True

#     def mark_as_borrowed(self):
#         self.is_available = False

#     def mark_as_returned(self):
#         self.is_available = True

#     def __str__(self):
#         return f"'{self.title}' by {self.author}"


# class Member:
#     def __init__(self, name, member_id):
#         self.name = name
#         self.member_id = member_id
#         self.borrowed_books = []

#     def borrow_book(self, book):
#         self.borrowed_books.append(book)

#     def return_book(self, book):
#         self.borrowed_books.remove(book)

#     def __str__(self):
#         return f"Member: {self.name} (ID: {self.member_id})"

# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []
#         self.members = []

#     def add_book(self, book):
#         self.books.append(book)
#         print(f"Added {book} to the library.")


# class Library():
#     def __init__(self, is_available):
#         self.is_available = is_available

# class Book(Library):
#     def __init__(self, name, author):
#         self.super()
#         self.name = name
#         self.author = author

# my_book = Book("a book", "me")
