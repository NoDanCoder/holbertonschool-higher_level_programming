#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    function that returns the weighted average of all integers
    tuple (<score>, <weight>)
    """
    mul = lambda x, y: x * y
    return (sum([mul(*x) for x in my_list]) / sum([x[1] for x in my_list])
            if my_list else 0)
