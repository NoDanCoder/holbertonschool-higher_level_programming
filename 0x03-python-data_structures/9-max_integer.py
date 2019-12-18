#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    function that finds the biggest integer of a list
    """
    add = 0
    for i in my_list:
        add = i if add < i else add
    return add if my_list else None
