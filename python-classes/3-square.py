#!/usr/bin/python3
# a class Square that defines a square by:
# based on 1-square.py
# size must be an integer, otherwise raise
# a TypeError exception with the message size must be an integer
# if size is less than 0,
# raise a ValueError exception with the message size must be >= 0
'''
    define a class 'Square'
'''


class Square:
    '''
      this is a class with an methods and attributes
    '''
    def __init__(self, size=0):
        '''
           this is an init method, it has private instance size
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
           a function that prints the area of the given square (current square)
        '''
        return (self.__size * self.__size)
