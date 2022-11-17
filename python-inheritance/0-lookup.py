#!/usr/bin/python3
# a function that returns the list of
# available attributes and methods of an object
"""
   define a function 'lookup'
"""


def lookup(obj):
    ''' this function prints the list of available attribute and methods '''
    return dir(obj)
