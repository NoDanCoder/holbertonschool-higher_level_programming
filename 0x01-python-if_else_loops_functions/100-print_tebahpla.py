#!/usr/bin/python3
for i in reversed(range(1, 27, 2)):
    print(str.format(chr(i + 97)), end="")
    print(str.format(chr(i - 1 + 65)), end="")
