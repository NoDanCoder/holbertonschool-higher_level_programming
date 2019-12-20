#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    function that deletes keys with a specific value in a dictionary
    """
    [a_dictionary.pop(k) for k, v in a_dictionary.copy().items() if v == value]
    return a_dictionary
