#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    function that computes the square value of all integers of a matrix
    """
    # map solution
    # return list(map(lambda y: list(map(lambda x: x**2, y)), matrix))
    return [[x**2 for x in y] for y in matrix]
