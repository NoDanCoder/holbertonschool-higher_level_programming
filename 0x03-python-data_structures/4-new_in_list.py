#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    function that replaces an element in a list at a
    specific position without modifying the original
    list (like in C).
    """
    my_new_list = my_list[:]
    if idx >= 0 and idx < len(my_list):
        my_new_list[idx] = element
    return my_new_list
