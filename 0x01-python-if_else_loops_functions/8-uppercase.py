#!/usr/bin/python3
def uppercase(str):
    str = list(str)
    str = [chr(ord(c) - 32) if ord(c) in range(ord('a'), ord('z') + 1) else c
           for c in str]
    print("".join(str))
