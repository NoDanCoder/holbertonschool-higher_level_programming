#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    function that prints all integers of a list
    """
    [print("{:d}".format(x)) for x in my_list]
