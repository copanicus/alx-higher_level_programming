#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent square"""

    def __init__(self, size=0):
        """Initilaize the new square.

        Args:
            size (int): The size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be greater than zero")
        self.__size = size
