#!/usr/bin/python3
def print_last_digit(number):
    lastDig = (number if number >= 0 else -number) % 10
    print("{:d}".format(lastDig), end='')
    return lastDig
