#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    number_of_arg = len(argv)
    if number_of_arg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    a = argv[1]
    b = argv[3]
    op = argv[2]
    if op == '+':
        print("{:d} {} {:d} = {:d}".format(a, op, b, add(a, b)))
    elif op == '-':
        print("{:d} {} {:d} = {:d}".format(a, op, b, sub(a, b)))
    elif op == '*':
        print("{:d} {} {:d} = {:d}".format(a, op, b, mul(a, b)))
    elif op == '/':
        print("{:d} {} {:d} = {:d}".format(a, op, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit (1)

