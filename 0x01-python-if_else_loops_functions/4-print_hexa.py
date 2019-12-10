#!/usr/bin/python3
i = 'a'
while ord(i) - 97 <= 98:
    print("{0:d} = 0x{0:x}".format(ord(i) - 97))
    i = chr(ord(i) + 1)
