#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    function that prints a matrix of integers
    """
    for y in matrix:
        print(str.format(" ".join(["{}".format(x) for x in y])))
