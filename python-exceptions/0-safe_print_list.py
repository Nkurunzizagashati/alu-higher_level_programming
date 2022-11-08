#!/usr/bin/python3
try:
    def safe_print_list(my_list=[], x=0):
        print(my_list)
        print(x)
except Exception as e:
    print(e)
