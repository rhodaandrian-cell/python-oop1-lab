# lib/coffee.py
# Defines the Coffee class for the Bookstore application.


class Coffee:
    """Represents a coffee object in the bookstore."""

    def __init__(self, size, price):
        """
        Initialize a Coffee instance.

        Args:
            size (str): The size of the coffee - must be Small, Medium, or Large.
            price (float): The price of the coffee.
        """
        self.size = size    # uses the property setter below
        self.price = price

    @property
    def size(self):
        """Get the size of the coffee."""
        return self._size

    @size.setter
    def size(self, value):
        """
        Set the size, ensuring it is Small, Medium, or Large.

        Args:
            value (str): The size value to set.
        """
        if value not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    def tip(self):
        """Add a tip — increases the price by 1."""
        print("This coffee is great, here's a tip!")
        self.price += 1