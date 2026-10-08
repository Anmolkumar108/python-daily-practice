class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def display_book(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
        }


class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            return "No books available in the library."
        return [book.display_book() for book in self.books]


book1 = Book(101, "Python Programming", "XYZ")
book2 = Book(102, "C Programming", "ABC")
book3 = Book(103, "Data Structures", "PQR")

library = Library("Sityog Library")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(f"Library Name: {library.library_name}")
print("Books in library:")
for book in library.books:
    print(book.display_book())

print("\nComplete library list:")
print(library.display_books())
