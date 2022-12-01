#!/usr/bin/python3
def weight_average(my_list=[]):
    return list(map(lambda x: list(map(lambda n: n**2, x)), my_list))
