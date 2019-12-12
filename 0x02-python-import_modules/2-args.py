#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    ac = len(argv) - 1
    print("{:d} arguments{}".format(ac, ":" if ac else "."))

    if ac:
        for i, av in enumerate(argv, 0):
            if av != argv[0]:
                print("{:d}: {}".format(i, av))
