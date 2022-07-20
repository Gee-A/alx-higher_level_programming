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
    def size(self, size):
        """Set the current size of the square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        size.__size = size

    def area(self):
        """ Returns the current square area """
        return (self.__size ** 2)
