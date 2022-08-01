#!/usr/bin/python3

"""Module 10-rectangle.py
Inherits from Rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square.
    Private instance attributes:
        -size
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """Initializes an instance of Square class
        Args:
            size: size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Utilizing Rectangle string method"""
        return str("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Computes the area of the Square instance.
        Overwrites the area() method from Rectangle.
        """
        return self.__size ** 2
