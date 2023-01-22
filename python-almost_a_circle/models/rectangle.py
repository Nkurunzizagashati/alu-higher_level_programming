#!/usr/bin/python3
# this file contains the Rectangle class
"""
    define class 'Rectangle'
"""
from models.base import Base


class Rectangle(Base):
    """
        this class inherits from Base class
    """
    def __ini__(self, width, height, x=0, y=0, id=None):
        """
            this init method contains private instance attributes
            height, width, x, and y.
        """
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """
            this is the getter method for height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            this method will help us to modify the value
            of height
        """
        if isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """
            this method will allow us to acces the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            we will call this function and pass in the value which
            we want to give to our width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """
            this method will help us to access the value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            this method is the one we will use to change the value
            of x(postion to x axis.)
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self, value):
        """
            this method is the one we will use to access the
            value of y(postion of object to y-axis)
        """
        self.__y = value

    @y.setter
    def y(self, value):
        """
            this method is the one we will call to
            modify the value of y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """
            this method will return the area of
            a rectangle
        """
        return (self.__height * self.__width)

    def display(self):
        """
            prints in stdout the Rectangle
            instance with the character #
        """
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
            this method will  returns [Rectangle] (<id>)
            <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """
            for now we are considering arguments and keyword arguments
            that assigns a key/value argument to attributes
        """
        if args:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
            this method will return the attributes of a rectangle
            in form of a dictionary, means with key value pair of the attributes.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
