#!/usr/bin/python3

"""Module 7-base_geometry
Defines simple instance method"""


class BaseGeometry:
    """A simple class defining two public instance method"""

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        Args:
            name: (string) gives definition to the type of value
            value: (int) must be validated
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
