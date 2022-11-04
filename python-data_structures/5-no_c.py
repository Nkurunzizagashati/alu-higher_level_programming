#!/usr/bin/python3
def no_c(my_string):
    new_str = [i for i in my_string if i.upper != "C"]
    print("".join(new_str))
