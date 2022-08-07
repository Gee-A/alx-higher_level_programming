#!/usr/bin/python3

"""Module rectangle
Create a class 'Rectangle' that inherit from the 'base'.
"""
from models.base import Base


class Rectangle(Base):
    """class describing a rectangle.
    Public intance method:
        - area
        - display
        - update
    Inherits from base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a rectangle instance
        Args:
            - __width: rectangle width
            - __height: rectangle height
            - __x: base cordinate
            - __y: coordinate along the abscissa coordinate
            - id: instance id
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Returns a formatted string of the Rectangle instance"""

        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return s

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

    def update(self, *args, **kwargs):
        """Updates attributes of an instance.
        Args:
            - id attribute
            - width attribute
            - height attribute
            - x attribute
            - y attribute
        """
        if args is not None and len(args) != 0:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of rectangle instance.
        """
        my_dict = {'x': self.__x, 'y': self.__y, 'id': self.id,
                   'height': self.__height, 'width': self.__width}
        return my_dict
