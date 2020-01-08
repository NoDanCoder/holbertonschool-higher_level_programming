#!/usr/bin/python3
def puts(elem):
    """ prints element and return 0 instead None """
    print(elem, end="")
    return 0


def safe_print_list(my_list=[], x=0):
    """ print safety x elements of a list, return amount printed elements """
    try:
        return sum([1 + puts(elem) for elem, idx in zip(my_list, range(x))])
    finally:
        print()
