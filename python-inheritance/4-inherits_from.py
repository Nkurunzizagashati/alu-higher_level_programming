#!/usr/bin/python3
# a function that returns True if the object
#  is an instance of a class that inherited (directly or indirectly)
#  from the specified class ; otherwise False
"""
  define a function 'inherits_from'
"""


def inherits_from(obj, a_class):
    """
       this function will check if an obj
       is an instance of a class that inherited derectly
       or inderectly
       return True or False
    """
    if isinstance(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
