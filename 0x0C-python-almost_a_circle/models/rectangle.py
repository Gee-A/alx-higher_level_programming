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
            - __width: rectangle width
            - __height: rectangle height
            - __x: a coordinate along the base
            - __y: a coordinate along the abscissa
            - id: instance id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Returns a formatted string format of instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

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
        return self.__y

    @width.setter
    def width(self, value):
        """Sets the width attributes."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height attribute."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x attribute."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y attribute."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Determines area of rectangle instance

        Returns: area
        """
        return self.__width * self.__height

    def display(self):
        """Prints rectangle instance using its attributes
        with the'#' character.
        """

        [print() for i in range(self.y)]
        [print(' '*self.x + '#'*self.width) for i in range(self.height)]
