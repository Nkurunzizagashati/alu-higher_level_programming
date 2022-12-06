#!/usr/bin/python3
# a class Rectangle that defines a rectangle, returns area
# and perimeter of a rectangle and for now
# it will draw a rectangle using h_tag
# it will have a public class attribute print_symbol
# it will have a methid that will compare two rectangles
"""
    define a class 'Rectangle'
"""


class Rectangle:
    """
        a class Rectangle with private attributes width and height
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
            this is the init function it is called as a class is called
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
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
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
            this method returns the area of rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
            this method returns the perimeter of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
            this method will draw the rectangle using h_tag
        """
        string = ''
        if self.__height == 0 or self.__width == 0:
            return string
        for i in range(0, self.__height):
            string += str(self.print_symbol) * self.width
            if i != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """
            this function will return the string representation of a rectangle
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """
            let say bye to the instance of
            Rectangle which will be passed in this function
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            this method will return the biggest REctangle
        """
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
            this method will returns a new
            Rectangle instance with width == height == size
        """
        return cls(size, size)
