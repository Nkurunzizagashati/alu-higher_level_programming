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
        return "[Square] ({}) {}/{} - {}/{}".format(self.id,
                                                    self.x, self.y,
                                                    self.width, self.height)

    @property
    def size(self):
        """
            this function will return the size of square
        """
        return self.height

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def __str__(self):
        """
            this is a special method
        """
        return "[Rectangle] ({}) {}/{} - {}".format(self.id, self.x, self.size)

    def update(self, *args, **kwargs):
        """
            let use *args, and **qwargs
        """
        if args is not None and len(args) is not 0:
            attributes = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if attributes[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
            this metho returns a dictionary
            representation of a rectangle
        """
        attributes = ['id', 'size', 'x', 'y']
        dict_repr = {}
        for key in attributes:
            if key == 'size':
                dict_repr[key] = getattr(self, 'width')
            else:
                dict_repr[key] = getattr(self, key)
        return dict_repr
