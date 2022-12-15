#!/usr/bin/python3
# This class will be the “base” of all other classes in this project
# The goal of it is to manage id attribute in all your future classes
# and to avoid duplicating the same code (by extension, same bugs)
"""
    define function 'Base'
"""


class Base:
    """
        this class Base is the base for all other classes
        in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            this init method has an attribute id which
            will show us the number of instnaces we have
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """
            static method  that returns the JSON string representation
            of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def create(cls, **dictionary):
        """
            this method writes the JSON string representation
            of list_objs to a file
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
