#!/usr/bin/python3
# a function that prints a square with the character '#'
"""
    define function 'print_square'
"""


def print_square(size):
    """
        this function will return the square represented by '#'
    """
    rect = ''
    n = 0
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    while n < size:
        print(size * '#')
        n += 1
