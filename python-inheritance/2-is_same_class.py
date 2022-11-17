#!/usr/bin/python3
# a function that returns True if the object is exactly
# an instance of the specified class ; otherwise False
"""
   define function 'is_same_class'
"""


def is_same_class(obj, a_class):
    """
       check whether an object is an instance of specified class
    """
    if type(obj) == a_class:
        return True
    return False
