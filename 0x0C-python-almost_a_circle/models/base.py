#!/usr/bin/python3

"""Module base
Creates a base class for all other classes in this project.
base manages the id attribute in all future classes and avoids
duplicating same code (by extension, same bugs)
"""

import json


class Base:
    """Class with:
    Private class attribute: __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance
        Args:
            - id: id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Encode to JSON format
        Args:
            - list_dictionaries

        Returns: JSON string representation of list_dictionaries.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Decode JSON string
        Args:
            - json_string: a string representing a list of dictionaries
        Return:
            - list representing json_string
            - (empty list) if string is None
        """
        dict_list = []
        if json_string is not None and json_string != '':
            dict_list = json.loads(json_string)
        return dict_list

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of list_objs to a file.
        Args:
            - list_objs: list of instances that inherits from Base
        """

        text = cls.to_json_string([o.to_dictionary() for o in list_objs])
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, "w") as f:
            f.write(text)
