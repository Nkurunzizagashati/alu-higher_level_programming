#!/usr/bin/python3
# a function that returns True if the object is an instance of,
# or if the object is an instance of a class that inherited from, the specified class
# otherwise False
"""
   define function 'is_kind_of_class''
"""


def is_kind_of_class(obj, a_class):
    """
       this function will rcheck whether object is instance of a_class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
