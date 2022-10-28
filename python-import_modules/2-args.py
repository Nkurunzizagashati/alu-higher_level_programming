#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    l = len(argv) - 1
    # l stad for length
    if l == 0:
        print("{}".format("0 arguments."))
    elif l == 1:
        print("{}".format("1 argument:"))
        print("{:d}: {}".format(l, argv[1]))
    else:
        print("{:d} arguments:".format(l))
        for i in range(1, l + 1):
            print("{:d}: {}".format(i, argv[i]))

