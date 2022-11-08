#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    var = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i], end=""))
            var += 1
        except Exception as e:
            print(e)
    print("")
    return var
