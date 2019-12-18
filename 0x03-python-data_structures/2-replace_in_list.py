#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    function that replaces an element of a list at a specific
    position (like in C)
    """
    if idx in range(len(my_list)):
        my_list[idx] = element
    return my_list
