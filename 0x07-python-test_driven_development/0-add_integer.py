#!/usr/bin/python3

"""Define an integer or float addition function"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.
    Float arguments are typecasted to ints before addition is perform.
    Raises:
        TypeError: if a and b is non-integer or non-float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer of float")
    return (int(a) + int(b))
