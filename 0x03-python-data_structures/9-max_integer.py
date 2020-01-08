#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    function that finds the biggest integer of a list
    """
    return None if not my_list else sorted(set(my_list))[-1]
