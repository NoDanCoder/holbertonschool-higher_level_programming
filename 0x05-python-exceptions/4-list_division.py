#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    function that divides element by element 2 lists
    and return a new one with the results
    """
    out = []
    val = 0
    for i in range(list_length):
        try:
            val = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except (ValueError, TypeError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            out.append(val)
            val = 0
    return out
