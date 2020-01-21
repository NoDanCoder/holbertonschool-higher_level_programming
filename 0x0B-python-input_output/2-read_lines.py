#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file (UTF8) and prints it to stdout """
    with open(filename, encoding="utf-8") as f:
        print(f.read(-1 if nb_lines == 0 else nb_lines))
