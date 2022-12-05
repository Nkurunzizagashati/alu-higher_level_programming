#!/usr/bin/python3
# a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""
    define a class 'Rectangle'
"""


class Rectangle:
    """
        a class Rectangle with private attributes width and height
    """

    def __init__(self, width=0, height=0):
        """
            this is the init function, it contains attributes and it is called as a class is called
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
            this method returns the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            this function will update the value of width
            if the value if not an integer, it will raise an error
            else if the value is less than zero it will raise ValueError
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
            this funcion will return the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            this function will update the value of height
            if value is not an integer, it will raise a TypeError
            else of value is less than zero, it will raise ValueError
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
