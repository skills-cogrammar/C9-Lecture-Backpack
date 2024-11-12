class Book:
    def __init__(self, title, author, copies=1):
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"{self.title} by {self.author} - Copies available: {self.copies}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book_title):
        for book in self.borrowed_books:
            if book.title.lower() == book_title.lower():
                self.borrowed_books.remove(book)
                return True
        return False

    def __str__(self):
        borrowed_books_title = ', '.join(book.title for book in self.borrowed_books)
        return f"Member: {self.name} (ID: {self.member_id}) - Borrowed books : {borrowed_books_title}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = {}

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' has been added to the library.")

    def add_member(self, member):
        if member.member_id not in self.members:
            self.members[member.member_id] = member
            print(f"Member '{member.name}' added to the library.")
        else:
            print(f"Member ID '{member.member_id}' already exists")

    def lend_book(self, title, member_id):
        member = self.members.get(member_id)
        if not member:
            print(f"Member ID '{member_id}' not found!")
            return

        for book in self.books:
            if book.title.lower() == title.lower() and book.copies > 0:
                book.copies -= 1
                member.borrow_book(book)
                print(f"Book '{title}' lent to member '{member.name}'")
                return

        print(f"Sorry, '{title}' is not available or out of stock!")

    """
    Extend the libary class by adding the following methods:
        1. return_book
        2. display_books
        3. display_members
        4. sell_old_books
    """


my_library = Library("The Cogrammar Library")

book1 = Book("Born a Crime", "Trevor Noah", 3)
book2 = Book("The Great Gatsby", "F. Scott", 2)
book3 = Book("The Problem with Nigeria", "Chinua Achebe", 3)
book4 = Book("1984", "George Orwell", 5)

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)
my_library.add_book(book4)

member1 = Member("Bonaventure Ogeto", "001")

my_library.add_member(member1)

my_library.lend_book("1984", "001")
my_library.lend_book("Born a Crime", "001")

print(my_library.members["001"])
