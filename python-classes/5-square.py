#!/usr/bin/python3
# a class Square that defines a square by: (based on 3-square.py)
# at this time we will add a private instance attribute
'''
   define a class 'Square'
'''


class Square:
    '''
       this class will contain __init_ module, and attributes
    '''
    def __init__(self, size=0):
        ''' this is an __init__ method , it has characters of an object '''
        self.size = size

    @property
    def size(self):
        ''' this is a private instance attribute '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' setting(mutating) the calue of the size '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        ''' a function that will print the area of the current square '''
        return (self.__size * self.__size)

    def my_print(self):
        ''' a method that the stdout the square with the # '''
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
