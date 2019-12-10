#!/usr/bin/python3
i = ['0', '0']
while ord(i[0]) <= ord('9'):
    i[1] = chr(ord(i[0]) + 1)

    while ord(i[1]) <= ord('9'):
        print("{}{}".format(i[0], i[1]), end='')

        if '9' in i[1] and '8' in i[0]:
            print()
        else:
            print(", ", end='')

        i[1] = chr(ord(i[1]) + 1)

    i[0] = chr(ord(i[0]) + 1)
