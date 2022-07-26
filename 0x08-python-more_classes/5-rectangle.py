#!/usr/bin/python3

"""
Module 5-rectangle.py defines a rectangle with a private instance attributes
and public instance method
"""


class Rectangle:
    """
        Rectangle class defined by width and height.
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

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a rectangle instance in '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ""
        rec_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += "#"
            rec_str += "\n"
        return rec_str[:-1]

    def __repr__(self):
        """
        Returns a string representation of a Rectangle instance that is able
        to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes a Rectangle instance."""
        print("Bye rectangle...")

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

    def area(self):
        """Calculates the area of a Rectangle instance
        Returns:
            Area of the rectangle.
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instance
        Returns:
            Perimeter, given by 2(h + w) and
            0 if any field is 0.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__height + self.__width))
