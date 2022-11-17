#!/usr/bin/python3
# a class MyList that inherits from list
# it will print the available attributed and methods for an object
"""
   define class 'list'
"""


class Mylist(list):
    """
       implement sorted list
    """

    def print_sorted(self):
        """
           prints sorted list
        """
        return sorted(self)
