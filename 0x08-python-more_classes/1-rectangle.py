#!/usr/bin/python3

"""
Module 1-rectangle.py defines a rectangle with a private instance attributes
"""


class Rectangle:
    """
        A basic rectangle with having attribute width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle object
        Args:
            width: represent width of new object
            height: represent height of new object
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
