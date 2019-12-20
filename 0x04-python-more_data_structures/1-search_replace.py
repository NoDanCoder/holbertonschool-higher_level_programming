#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    function that replaces all occurrences of an element
    by another in a new list
    """
    # map solution
    # return list(map(lambda x: x if x != search else replace, my_list))
    return [x if x != search else replace for x in my_list]
