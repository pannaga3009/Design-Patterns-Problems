from abc import ABC, abstractmethod
from typing import List, Set


class Book:
    def __init__(self, title: str, page_count: int):
        self.title = title
        self.page_count = page_count


class BookFilter(ABC):
    @abstractmethod
    def apply(self, book: Book) -> bool:
        pass


class TitleFilter(BookFilter):
    def __init__(self, title: str):
        self.title_keyword = title

    def apply(self, book: Book) -> bool:
        return self.title_keyword.lower() in book.title.lower()


class BookSize:
    BIG = "Big"
    MEDIUM = "Medium"
    SMALL = "Small"


class BookSizeFilter(BookFilter):
    def __init__(self, desired_size: str):
        self.desired_size = desired_size

    def apply(self, book: Book) -> bool:
        size_ranges = {
            BookSize.BIG: (0, 100),
            BookSize.MEDIUM: (101, 500),
            BookSize.SMALL: (501, float('inf'))
        }
        min_pages, max_pages = size_ranges.get(self.desired_size, (0, float('inf')))
        print(f"min pages {min_pages} and max_pages {max_pages}")
        print(f"{min_pages} <= {book.page_count} < {max_pages}")
        return min_pages <= book.page_count < max_pages


def book_passes_filters(book: Book, filters: List[BookFilter]) -> bool:
    for book_filter in filters:
        if not book_filter.apply(book):
            return False
    return True


def filter_books(book_list: List[Book], filters: List[BookFilter]) -> Set[Book]:
    filtered_books = set()
    for book in book_list:
        if book_passes_filters(book, filters):
            filtered_books.add(book)
    return filtered_books


# Example Usage
if __name__ == "__main__":
    books = [
        Book("The Big Journey", 120),
        Book("Medium Tales", 320),
        Book("Tiny Adventures", 70),
        Book("The Great wall", 50)
    ]

    filters = [TitleFilter("Great"), BookSizeFilter(BookSize.BIG)]

    filtered_books = filter_books(books, filters)

    for book in filtered_books:
        print(f"Book: {book.title}, Pages: {book.page_count}")
