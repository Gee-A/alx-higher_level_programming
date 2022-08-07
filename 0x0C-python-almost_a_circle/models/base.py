#!/usr/bin/python3

"""Module base
Creates a base class for all other classes in this project.
base manages the id attribute in all future classes and avoids
duplicating same code (by extension, same bugs)
"""

import json
import os
import csv


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
        if (type(list_dictionaries) != list or
           not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
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
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            dict_list = json.loads(json_string)
        return dict_list

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of list_objs to a file.
        Args:
            - list_objs: list of instances that inherits from Base
        """
        """
        if type(list_objs) != list and list_objs is not None:
            raise TypeError("list_objs must be a list of instances")
        if any(issubclass(type(x), Base) is False for x in list_objs):
            raise TypeError("list_objs must be a list of instances")
        """
        if list_objs is None or list_objs == []:
            jstr = "[]"
        else:
            jstr = cls.to_json_string([o.to_dictionary() for o in list_objs])
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, "w") as f:
            f.write(jstr)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        Args:
            - dictionary: used as **kwargs

        Returns: instance created
        """
        # must need width and height assigned that must not be <= 0
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        # must need size assigned
        if cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""

        file_name = cls.__name__ + ".json"
        my_list = []
        dict_list = []
        if os.path.exists(file_name):
            with open(file_name) as f:
                s = f.read()
                dict_list = cls.from_json_string(s)
                for d in dict_list:
                    my_list.append(cls.create(**d))
        return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs in CSV format
        and saves to file.
        Args:
            - list_objs: list of instances that inherits from Base
        """

        if (type(list_objs) != list and
           list_objs is not None or
           not all(isinstance(o, cls) for o in list_objs)):
            raise TypeError("list_objs must be a list of instances")

        file_name = "{}.csv".format(cls.__name__)
        with open(file_name, "w", newline='') as f:
            if list_objs is not None:
                dict_list = [o.to_dictionary() for o in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(dict_list)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file.

        Returns: list of intances
        """

        file_name = "{}.csv".format(cls.__name__)
        my_list = []
        if os.path.exists(file_name):
            with open(file_name, newline='') as f:
                reader = csv.reader(f, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for i, v in enumerate(reader):
                    if i > 0:
                        # Be it Rectangle or square
                        o = cls(1, 1)
                        for k, w in enumerate(v):
                            if w:
                                setattr(o, fields[k], int(w))
                        my_list.append(o)
        return my_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws all Rectangles and Squares.
        Opens a windows
        Args:
            - list_rectangles: list of rectangle instance to draw
            - list_squares: list of square instance to draw
        """
        import turtle
        import time
        from random import randrange

        t = turtle.Turtle()
        t.color("white")
        turtle.bgcolor("black")
        t.shape("turtle")
        t.pensize(3)

        for i in (list_rectangles + list_squares):
            t.penup()
            t.setpos(0, 0)
            turtle.Screen().colormode(255)
            t.pencolor((randrange(255), randrange(255), randrange(255)))
            Base.draw_rect(t, i)
            time.sleep(1)
        time.sleep(5)

    @staticmethod
    def draw_rect(t, rect):
        """Helper method that draws a Rectangle
        or Square.

        TODO: Ensure shape does not intersect
        """

        t.penup()
        t.setpos(rect.x, rect.y)
        t.pendown()
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
