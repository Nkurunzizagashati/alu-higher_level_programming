#!/usr/bin/python3
# a function that adds 2 integers
"""
    define function 'add_integers'
"""


def add_integer(a, b=98):
    """
        this function returns the sum of two integers
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if not isinstance(a, int):
        raise TypeError('a must be an integer')
    if not isinstance(b, int):
        raise TypeError('b must be an integer')
    return (a + b)
