#!/usr/bin/python3
def safe_print_integer(value):
    """ prints safety a number """
    try:
        print("{:d}".format(value), end="")
        return True
    except (ValueError, TypeError):
        return False


def safe_print_list_integers(my_list=[], x=0):
    """
    print safety upto "x" elements of a list, only if they are integers
    return amount printed elements
    """
    buff = [1 for i in range(x) if safe_print_integer(my_list[i])]
    print()
    return sum(buff)
