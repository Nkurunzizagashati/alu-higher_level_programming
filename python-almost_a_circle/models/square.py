#!/usr/bin/python3
# the class Square that inherits from Rectangle
"""
    define class 'Square'
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        this function defines square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            this is an init function, it will
            be given some attributes from Rectangle function
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            magic method
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                    self.x, self.y,
                                                    self.height)
                                                    
