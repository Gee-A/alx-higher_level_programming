#!/usr/bin/python3

""" Defining a Square class """


class Square:
    """ Represent an empty square class """

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the current size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the current square area """
        return (self.__size ** 2)

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparision to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparision to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparision to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparision to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparision to a Square."""
        return self.area() >= other.area()
