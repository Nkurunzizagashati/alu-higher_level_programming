#!/usr/bin/python3
# a class MyList that inherits from list
# it will print the available attributed and methods for an object
"""
   define class 'list'
"""


class Mylist(list):
    ''' this class inherits from 'list' class '''

    def print_sorted(self):
        ''' return: sorted list '''
        return sorted(self)
