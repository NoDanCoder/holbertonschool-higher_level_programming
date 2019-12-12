#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv as av
    print("{}".format(sum([int(x) for x in av[1:]])))
