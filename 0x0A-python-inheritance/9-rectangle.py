#!/usr/bin/python3

"""Module 8-rectangle.py
Inherits from BaseGeometry to"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle.
    Private instance attributes:
        - width
        - height
    Inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """Initializes an instance of Rectangle class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ Returns a formatted string."""
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Computes the area of the Rectangle instance.
        Overwrites the area() method from BaseGeometry.
        """
        return self.__width * self.__height
