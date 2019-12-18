#!/usr/bin/python3
def element_at(my_list, idx):
    """
    function that retrieves an element from a list like in C
    """
    if idx in range(len(my_list)):
        return my_list[idx]
