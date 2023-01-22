#!/usr/bin/python3
"""Square Module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class to model a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialise class

        Description:
            This method is the class constructor which initialises
            the class with the required parameters. This class
            inherits all the properties from the super class

        Args:
            size (int): the size of the square
            x (int): the x coordinate of the square
            y (int): the y coordinate of the square
            id (int): the instance tracker
        """

        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """Get size

        Description:
            This method obtains the size of the square object by
            invoking the width method from the super class

        Returns:
            The size of this square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Set size

        Description:
            This method sets the size of the square object by
            invoking the height and the width methods of the
            super class

        Args:
            value (int): a positive integer value

        Raises:
            TypeError for an invalid data type
            ValueError for an invalid value: 0 or less
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign to each attribute

        Description:
            This method assigns an argument to each attribute
            of the square object

        Args:
            args (int): a variable length of integer arguments
            kwargs (collection): a collection of key/value objects
            1st argument represents the id attribute
            2nd argument represents the size attribute
            3rd argument represents the x attribute
            4th argument represents the y attribute
        """

        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                    self.height = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        else:
            for val, vals in kwargs.items():
                if val == "id":
                    self.id = vals
                elif val == "size":
                    self.width = vals
                    self.height = vals
                elif val == "x":
                    self.x = vals
                elif val == "y":
                    self.y = vals

    def to_dictionary(self):
        """Dictionary representation

        Description:
            This method creates a dictionary representation
            of this square object

        Returns:
            A dictionary object of square
        """
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """Return a string representation of this rectangle"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)
