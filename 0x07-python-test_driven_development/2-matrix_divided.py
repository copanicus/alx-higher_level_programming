#!/usr/bin/python3
#2-matrix_divided.py
"""Define matrix division function"""


def matrix_divided(matrix, div):
    """Divide all element in the matrix.
    Args:
        matrix (list): is a list of list of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If the div is not an int or a float.
        ZeroDivisionError: If the div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError("matrix must be a matrix (list of list) of (integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("each row of the matrix must be of same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(i / div, 2) for i in row] for row in matrix]
    return (new_matrix)
