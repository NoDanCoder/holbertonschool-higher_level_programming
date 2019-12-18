#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    function that prints a matrix of integers
    """
    [print((" ".join(["{}"] * len(y))).format(*y)) for y in matrix]
