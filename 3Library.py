class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display(self):
        print(f"Book Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")

def input_book_details():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    isbn = input("Enter the ISBN of the book: ")
    return Book(title, author, isbn)

Library = []
n = int(input("Enter the number of books: "))
for i in range(1, n + 1):
    print(f"\nEnter details for book {i}:")
    book = input_book_details()
    Library.append(book)

print("\nBooks in the library:")
for book in Library:
    book.display()