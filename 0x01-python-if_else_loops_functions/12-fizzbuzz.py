#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        msg = "Fizz" if x % 3 == 0 else ""
        msg += "Buzz" if x % 5 == 0 else ""
        msg = str(x) if not msg else msg
        print("{} ".format(msg), end='')
