#!/usr/bin/python3
def no_c(my_string):
    """
    function that removes all characters c and C from a string
    """
    return "".join([x for x in my_string if x != "C" and x != "c"])
