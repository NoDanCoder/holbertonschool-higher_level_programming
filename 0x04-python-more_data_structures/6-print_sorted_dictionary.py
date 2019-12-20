#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    function that prints a dictionary by ordered keys
    first parent level only
    """
    if a_dictionary:
        [print("{}: {}".format(k, v)) for k, v in sorted(a_dictionary.items())]
