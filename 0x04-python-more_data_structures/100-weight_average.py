#!/usr/bin/python3
def mul(x, y):
    """
    function that returns "x" multiplied by "y"
    """
    return x * y


def weight_average(my_list=[]):
    """
    function that returns the weighted average of all integers
    tuple (<score>, <weight>)
    """
    return (sum([mul(*x) for x in my_list]) / sum([x[1] for x in my_list])
            if my_list else 0)
