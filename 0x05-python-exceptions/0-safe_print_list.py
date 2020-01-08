#!/usr/bin/python3
def puts(elem, buff):
    """ prints element and return 0 instead None """
    print(elem, end="")
    buff.append(1)
    return 0


def safe_print_list(my_list=[], x=0):
    """ print safety x elements of a list, return amount printed elements """
    try:
        buff = []
        [puts(my_list[i], buff) for i in range(x)]
    except IndexError:
        pass
    finally:
        print()
        return sum(buff)
