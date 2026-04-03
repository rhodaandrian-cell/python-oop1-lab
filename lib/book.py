# lib/book.py
# Defines the Book class for the Bookstore application.


class Book:
    """Represents a book object in the bookstore."""

    def __init__(self, title, page_count):
        """
        Initialize a Book instance.

        Args:
            title (str): The title of the book.
            page_count (int): The total number of pages in the book.
        """
        self.title = title
        self.page_count = page_count  # uses the property setter below

    @property
    def page_count(self):
        """Get the page count of the book."""
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """
        Set the page count, ensuring it is an integer.

        Args:
            value: The page count value to set.
        """
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        """Simulate turning a page in the book."""
        print("Flipping the page...wow, you read fast!")