#!/usr/bin/python3
i = 'a'
while ord(i) - 97 < 99:
    print("{:02d}, ".format(ord(i) - 97), end='')
    i = chr(ord(i) + 1)

print("{0:02d}".format(ord(i) - 97))
