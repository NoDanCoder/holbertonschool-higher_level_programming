#!/usr/bin/python3
"""
The math operations module
==========================
this module has an add_integer fucn just for now
"""


def add_integer(a, b=98):
    """
    Funtion that adds 2 integers or/and floats.
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    a = int(a) if type(a) != int else a
    b = int(b) if type(b) != int else b

    return a + b
