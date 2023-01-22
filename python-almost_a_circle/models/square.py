#!/usr/bin/python3
"""
    define class Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
        this is class Square that inherits Rectangle
        class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            we will us super to inherit the attributes of the
            Rectangle class.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            this method will help us to access the size
            of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            we will call this method and pass a value we
            want to give our size attribute
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
            this method will return
            [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """
            the 1st arument must be id
            2nd argument must be size
            3rd armument must be x
            4th argument must be y
            if args is present kwargs will not be considered
            else, its values will be assigned to Square attributes.
        """
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

        elif len(kwargs) != 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            else:
                self.id

            if "size" in kwargs:
                self.size = kwargs["size"]
            else:
                self.size

            if "x" in kwargs:
                self.x = kwargs["x"]
            else:
                self.x

            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
            this method will return the attributes of a square
            in form of a dictionary, means with
            key value pair of the attributes.
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
