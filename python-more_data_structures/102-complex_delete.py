#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in a_dictionary.keys():
        if value in a_dictionary[i]:
            if a_dictionary[i] == value:
                del a_dictionary[i]
        return a_dictionary
