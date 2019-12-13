#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as av
    from calculator_1 import add, sub, mul, div
    if len(av) == 4:
        a, b = int(av[1]), int(av[3])
        if av[2] == "+":
            result = add(a, b)
        elif av[2] == "-":
            result = sub(a, b)
        elif av[2] == "*":
            result = mul(a, b)
        elif av[2] == "/":
            result = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

        print("{:d} {} {:d} = {:d}".format(a, av[2], b, result))

    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
