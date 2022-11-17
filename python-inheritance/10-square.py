#!/usr/bin/python3
# a class Square that inherits from Rectangle (9-rectangle.py)
# the area() method must be implemented
"""
   define a class 'Square'
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
       this class will define the area of rectangle
    """

    def __init__(self, size):
        """
           this method contains attribute size
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
