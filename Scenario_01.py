class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def categorize(self):
        if self.price >= 500:
            return "Premium"
        else:
            return "Standard"
        
    def display(self):
        print("Book ID    :", self.book_id)
        print("Title      :", self.title)
        print("Author     :", self.author)
        print("Price      :", self.price)
        print("Category   :", self.categorize())
        print("-" * 30)

class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Library Name:", self.library_name)
        print("=" * 30)

        for book in self.books:
            book.display()

# Creating Library object
library = Library("City Library")
# Creating Book objects
b1 = Book(101, "Python Programming", "John Smith", 650)
b2 = Book(102, "Data Structures", "Robert Brown", 450)
b3 = Book(103, "Computer Networks", "James Lee", 800)
b4 = Book(104, "Database Systems", "David Kumar", 350)

# Adding books to library
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)
library.add_book(b4)

# Display all books
library.display_books()