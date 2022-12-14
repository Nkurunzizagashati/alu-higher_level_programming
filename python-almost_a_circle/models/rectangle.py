#!/usr/bin/python3
# class Rectangle that inherits from Base
# Private instance attributes, each with its own public
# getter and setter(__width -> width, __height -> height,
# __x -> x, __y -> y)
"""
    importing 'base' file which has Base class
"""

from models.base import Base
"""
    define class 'Rectangle'
"""


class Rectangle(Base):
    """
        this function inherits from Base class, it has an init method
        with private attriutes
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            this is an init method
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            through this functtion we will get the value of width
        """
        return self.__width

    @width.setter
    def width(self, new_width):
        """
            the user will pass the new width value
            in this function which will replace the
            existing value
        """
        if not isinstance(new_width, int):
            raise TypeError("width must be an integer")
        if new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    @property
    def height(self):
        """
            through this function, you can access the calue of height
        """
        return self.__height

    @height.setter
    def height(self, n_height):
        """
            this function will update the value of height
        """
        if not isinstance(n_height, int):
            raise TypeError("height must be an integer")
        if n_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = n_height

    @property
    def x(self):
        """
            this function will read the position
            on x_axis
        """
        return self.__x

    @x.setter
    def x(self, new_x):
        """
            this function will update the position
            on x_axis
        """
        if not isinstance(new_x, int):
            raise TypeError("x must be an integer")
        if new_x <= 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    @property
    def y(self):
        """
            this function will return the value of y
            which is the position on y_axis
        """
        return self.__y

    @y.setter
    def y(self, new_y):
        """
            this function updates the value of y
        """
        if not isinstance(new_y, int):
            raise TypeError("y must be an int")
        if new_y <= 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y
