#!/usr/bin/python3
def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8) and returns
    the number of characters added """
    with open(filename, "a", enconding="utf-8"):
        return f.write(text)
