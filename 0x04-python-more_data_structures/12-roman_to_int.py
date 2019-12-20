#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    function that converts a Roman numeral to an integer
    """
    if roman_string and isinstance(roman_string, str):
        num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        word = list(reversed(roman_string))
        add = num[word[0]]
        for i, n in zip(word, word[1:]):
            add += num[n] * (1 if num[i] <= num[n] else -1)
        return add
    return 0
