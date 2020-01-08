#!/usr/bin/python3
def safe_print_division(a, b):
    """ print safety a div operation """
    try:
        var = a / b
    except ZeroDivisionError:
        var = None
    finally:
        print("Inside result: {}".format(var))
        return var
