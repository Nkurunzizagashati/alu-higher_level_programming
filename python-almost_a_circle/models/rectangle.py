#!/usr/bin/python3
"""define class rectangle"""

from models.base import Base


class Rectangle(Base):
    """this class inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            this method will help us to acess the width
            attribute
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
            this method will help us to modify
            the width attribute
        """

        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
            this method will help us to acess the height
            attrbute
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
            this method will help us to  modify
            the height attribute
        """

        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
            this method will help us to acess the
            x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            this method will help us
            to modify the x attribute
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """acessing y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """modifying y attribute"""

        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
            this mehtod will return the area of
            rectangle
        """
        return self.width * self.height

    def display(self):
        """return rectangle in form of #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
            this method will  returns [Rectangle] (<id>)
            <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
            for now we are considering arguments and keyword arguments
            that assigns a key/value argument to attributes
        """
        if len(args) != 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        elif len(kwargs) != 0:
            self.id = kwargs["id"] if "id" in kwargs else self.id
            self.width = kwargs["width"] if "width" in kwargs \
                else self.width
            self.height = kwargs["height"] if "height" in kwargs \
                else self.height
            self.x = kwargs["x"] if "x" in kwargs else self.x
            self.y = kwargs["y"] if "y" in kwargs else self.y

    def to_dictionary(self):
        """
            this method will return the attributes of a rectangle
            in form of a dictionary, means with key value
            pair of the attributes.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
