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
    def width(self, value):
        """
            the user will pass the new width value
            in this function which will replace the
            existing value
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
            through this function, you can access the calue of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            this function will update the value of height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
            this function will read the position
            on x_axis
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            this function will update the position
            on x_axis
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
            this function will return the value of y
            which is the position on y_axis
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            this function updates the value of y
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
            this method calculates the area of a square
        """
        return self.height * self.width

    def display(self):
        """
            prints in stdout the Rectangle instance with the
            character # - you don’t need to handle x and y here
        """
        if self.height == 0 or self.width == 0:
            print("")
            return [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for n in range(self.x)]
            [print("#", end="") for m in range(self.width)]
            print("")

    def __str__(self):
        """
            this function will print the string representation
            class Rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                 self.x, self.y, self.width, self.height)
