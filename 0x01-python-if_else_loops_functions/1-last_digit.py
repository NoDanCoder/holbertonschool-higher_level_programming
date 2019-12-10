#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDig = int(repr(number)[-1])
msg = "and is " + (
    "greater than 5" if lastDig > 5
    else "0" if lastDig == 0 else "less than 6 and not 0")
print("Last digit of {0:d} is {1:d} {2}".format(number, lastDig, msg))
