#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize the new square.
        Args:
            size (int): Size of the new square.
        """
        self.size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of a square."""
        return (self.__size ** 2)
