#!/usr/bin/python3
"""
The math operations module 2
============================
this module has a matrix_divided fucn just for now
"""


def matrix_divided(matrix, div):
    """
    Funtion that divide 2 matrix integers or/and floats.
    """
    if type(matrix) != list or \
       not all(type(y) is list and y != [] for y in matrix) or \
       not all(all(type(x) is int or type(x) is float for x in y)
               for y in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    elif not all(len(y) == len(matrix[0]) for y in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    elif (type(div) != int and type(div) != float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    return [[float("{:.2f}".format(x / div)) for x in y] for y in matrix]
