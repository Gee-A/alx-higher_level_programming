#!/usr/bin/python3

"""Module base
Creates a base class for all other classes in this project.
base manages the id attribute in all future classes and avoids
duplicating same code (by extension, same bugs)
"""


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
