#!/usr/bin/python3
try:
    def safe_print_list(my_list=[], x=0):
        print(x, end="")
except Exception as e:
    print(e)
