from abc import ABC, abstractmethod  # Importing Abstract Base Class (ABC) and abstractmethod decorator
from typing import List, Set  # Importing List and Set types for type hints


# Book class represents a book with a title and page count
class Book:
    def __init__(self, title: str, page_count: int):
        self.title = title  # Book title
        self.page_count = page_count  # Number of pages in the book


# BookFilter is an abstract base class that defines a common interface for all filters
class BookFilter(ABC):
    @abstractmethod
    def apply(self, book: Book) -> bool:
        """
        Abstract method that must be implemented by all subclasses.
        Takes a Book object as input and returns a boolean indicating 
        whether the book meets the filter criteria.
        """
        pass


# TitleFilter is a concrete class that filters books based on their title
class TitleFilter(BookFilter):
    def __init__(self, title: str):
        self.title_keyword = title  # Keyword to search for in the book title

    def apply(self, book: Book) -> bool:
        """
        Checks if the book's title contains the specified keyword.
        Returns True if the keyword is found, otherwise False.
        """
        return self.title_keyword.lower() in book.title.lower()


# BookSize is a utility class that defines different size categories for books
class BookSize:
    BIG = "Big"        # Represents books with 0 to 100 pages
    MEDIUM = "Medium"  # Represents books with 101 to 500 pages
    SMALL = "Small"    # Represents books with more than 500 pages


# BookSizeFilter is a concrete class that filters books based on their size
class BookSizeFilter(BookFilter):
    def __init__(self, desired_size: str):
        self.desired_size = desired_size  # The desired size category (BIG, MEDIUM, or SMALL)

    def apply(self, book: Book) -> bool:
        """
        Checks if the book's page count falls within the range defined by the desired size.
        Returns True if the book's page count is within the range, otherwise False.
        """
        # Define the page count ranges for each book size category
        size_ranges = {
            BookSize.BIG: (0, 100),
            BookSize.MEDIUM: (101, 500),
            BookSize.SMALL: (501, float('inf'))
        }
        
        # Get the min and max pages for the desired size category
        min_pages, max_pages = size_ranges.get(self.desired_size, (0, float('inf')))
        
        # Print statements for debugging purposes
        print(f"min pages {min_pages} and max_pages {max_pages}")
        print(f"{min_pages} <= {book.page_count} < {max_pages}")
        
        # Check if the book's page count falls within the range
        return min_pages <= book.page_count < max_pages


# Function to check if a book passes all the given filters
def book_passes_filters(book: Book, filters: List[BookFilter]) -> bool:
    """
    Checks if a book passes all the provided filters.
    Returns True if the book satisfies all filters, otherwise False.
    """
    for book_filter in filters:
        if not book_filter.apply(book):  # If any filter fails, return False
            return False
    return True  # If all filters pass, return True


# Function to filter a list of books based on a list of filters
def filter_books(book_list: List[Book], filters: List[BookFilter]) -> Set[Book]:
    """
    Filters a list of books using the provided list of filters.
    Returns a set of books that satisfy all filters.
    """
    filtered_books = set()  # Initialize an empty set to store filtered books
    for book in book_list:
        if book_passes_filters(book, filters):  # If the book passes all filters, add it to the set
            filtered_books.add(book)
    return filtered_books  # Return the set of filtered books


# Example Usage: Demonstrating how to filter books using the defined filters
if __name__ == "__main__":
    # Create a list of Book objects
    books = [
        Book("The Big Journey", 120),
        Book("Medium Tales", 320),
        Book("Tiny Adventures", 70),
        Book("The Great Wall", 50)
    ]

    # Define filters to apply: TitleFilter to find books with "Great" in the title and BookSizeFilter for "BIG" books
    filters = [TitleFilter("Great"), BookSizeFilter(BookSize.BIG)]

    # Apply the filters to the list of books
    filtered_books = filter_books(books, filters)

    # Print the filtered books
    for book in filtered_books:
        print(f"Book: {book.title}, Pages: {book.page_count}")
