#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    number_of_arg = len(argv)
    if number_of_arg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit (1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op == '+':
        answer = add(a, b)
    elif op == '-':
        answer = sub(a, b)
    elif op == '*':
        answer = mul(a, b)
    elif op == '/':
        answer = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit (1)
    print("{:d} {} {:d} = {:d}".format(a, op, b, answer))
