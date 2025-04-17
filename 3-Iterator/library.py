from abc import ABC, abstractmethod
from typing import List


# Imagine we have a list of books in a digital library,
#  and we want to iterate over them one by one without exposing the internal structure of the list.

# Iterator Interface
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass

# Iterable Interface
class Iterable(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass

# Book class representing a single book
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f'"{self.title}" by {self.author}'

# Collection of Books implementing Iterable
class BookCollection(Iterable):
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def create_iterator(self) -> Iterator:
        return BookIterator(self.books)

# Concrete Iterator for BookCollection
class BookIterator(Iterator):
    def __init__(self, books: List[Book]):
        self._books = books
        self._index = 0

    def has_next(self) -> bool:
        return self._index < len(self._books)

    def next(self):
        if self.has_next():
            book = self._books[self._index]
            self._index += 1
            return book
        else:
            raise StopIteration("No more books in the collection")

# Main Execution
if __name__ == "__main__":
    # Create a book collection
    library = BookCollection()
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

    # Get an iterator
    iterator = library.create_iterator()

    # Iterate through books
    while iterator.has_next():
        print(iterator.next())
