#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    else:
        n_tuples = len(my_list)
        x = 0
        result = 0
        f_p = 0
        while x < n_tuples:
            m = my_list[x][0] * my_list[x][1]
            result += m
            p = my_list[x][1]
            f_p += p
            x += 1
        return result/f_p
