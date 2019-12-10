#!/usr/bin/python3
for i in range(26):
    if not chr(i + 97) in "eq":
        print(str.format(chr(i + 97)), end="")
