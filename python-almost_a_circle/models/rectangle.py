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
