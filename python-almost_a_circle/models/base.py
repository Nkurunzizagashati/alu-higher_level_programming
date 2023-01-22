#!/usr/bin/python3
# This class will be the “base” of all other classes in this project
# The goal of it is to manage id attribute in all your future classes
# and to avoid duplicating the same code (by extension, same bugs)
"""
    define base class
"""
import json
import csv


class Base:
    """
        this is the base class, it contains an init method
        and a private class attribute nb_objects which is the
        number of objects.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
            this is an init method with id attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            this method will convert a list of dictionary
            to json_string representation.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            this method will help us to save our list_objs[list of
            objects(they are our classes which have inherited from this base
            class)] which are in json form to a file with a '.json' extension.
            first of all we will change the file(ex: rectangle, square) to a
            json file and then save them(write them) to a file.
            The filename must be: <Class name>.json - example: Rectangle.json   
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)
        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
            this method returns the list of the JSON string representation
            json_string is a string representing a list of dictionaries,
            If json_string is None or empty,the method returns an empty list,
            Otherwise, it returns the list represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """
            this method 
        """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                json_string = f.read()
        except:
            return []
        json_list = cls.from_json_string(json_string)
        return [cls.create(**d) for d in json_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            save to csv
        """
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            fieldnames = ["id", "size", "x", "y"]
        else:
            fieldnames = ["id"]
        with open(filename, "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls): 
        """
            load from csv
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as csvfile:
                reader = csv.DictReader(csvfile)
                list_objs = [cls.create(**d) for d in reader]
        except:
            return []
        return list_objs
