#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    function that adds 2 tuples
    - If a tuple is smaller than 2, use the value 0 for each missing integer
    - If a tuple is bigger than 2, use only the first 2 integers
    """
    list_a = list(tuple_a) + ([0] * (-len(tuple_a) + 2))
    list_b = list(tuple_b) + ([0] * (-len(tuple_b) + 2))
    return tuple(x + y for (x, y) in zip(list_a, list_b))
