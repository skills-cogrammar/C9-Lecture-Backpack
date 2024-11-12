'''
LIBRARY MANAGEMENT SYSTEM
'''

# Book object
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_available = True
    
    def lend_book(self):
        '''
        Lends a book to a member
        Checks if the book is available
        '''
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def return_book(self):
        '''
        Sets the attribute is_available to True when a member returns a book
        '''
        self.is_available = True

# Library object
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        '''
        Method to add a new book to the library
        '''
        self.books.append(book)
        print(f"Added a book: {book.title} by {book.author} the genre {book.genre}\n")
    
    def list_all_books(self):
        '''
        Method is supposed to iterate over the books list and display all books.
        '''
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Available: {book.is_available}\n")


# Person Object
class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id


# Member Object
class Member(Person):
    def __init__(self, name, person_id, member_id):
        super().__init__(name, person_id)
        self.member_id = member_id
        self.borrowed_books = []

    
    def borrow_book(self, book):
        '''
        Checks is the books is available for borrowing
        Appends to the member's list of borrowed books
        sets the status of the book to not available
        '''
        if book.is_available:
            self.borrowed_books.append(book)
            book.lend_book()
            print(f"{self.name} has borrowed {book.title}")
        else:
            print(f"{book.title} is not available for borowing")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{book.title} has been returned")



# Staff Object
'''
TO DO: Give the staff some work to do
'''
class Staff(Person):
    def __init__(self, name, person_id, staff_id):
        super().__init__(name, person_id)
        self.staff_id = staff_id


# Creating instances of members
member1 = Member("Dan", 1, 101)
member2 = Member("Bonaventure", 2, 102)




# Creating instances of books
harry_potter = Book('Harry Potter', 'J.K Rowling', 'Fantasy')
origin = Book('Origin', 'Dan Brown', 'Fantasy')
game_of_thrones = Book('G.O.T', 'George RR Martin', 'Action')
hunger_games = Book('Hunger Games', 'Suzanne Collins', 'Action')

# Create an instance of a library
co_grammar_library = Library()

print("Adding Books \n\n")
co_grammar_library.add_book(harry_potter)
co_grammar_library.add_book(origin)
co_grammar_library.add_book(game_of_thrones)
co_grammar_library.add_book(hunger_games)

print("Listing Books \n\n")

co_grammar_library.list_all_books()


# Borrow books
member1.borrow_book(harry_potter)

print("Listing borrowed Books \n\n")

co_grammar_library.list_all_books()

# Return book
member1.return_book(harry_potter)

print("Listing Books \n\n")

co_grammar_library.list_all_books()