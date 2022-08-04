#!/usr/bin/python3

"""Module rectangle
Create a class 'Rectangle' that inherit from the 'base'.
"""
from models.base import Base


class Rectangle(Base):
    """class describing a rectangle.
    Public intance method:
    Inherits from base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a rectangle instance
        Args:
            __width (int): rectangle width
            __height (int): rectangle height
            __x (int): a coordinate along the base
            __y (int): a coordinate along the abscissa
            - id: instance id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """Get the width attribute."""
            return self.__width

        @property
        def height(self):
            """Get the height attribute."""
            return self.__height

        @property
        def x(self):
            """Get the x attribute."""
            return self.__x

        @property
        def y(self):
            """Get the y attribute."""
            return self.__x

        @width.setter
        def width(self, value):
            self.__width = value

        @height.setter
        def height(self, value):
            self.__height = value

        @x.setter
        def x(self, value):
            self.__x = value

        @y.setter
        def y(self, value):
            self.__y = value
