#!/usr/bin/python3

"""Module square
Create a Square class, inheriting from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class describing a square.
    Inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square instance.
        Args:
            - __size: size of square
            - __x: base coordinate
            - __y: abscissa coordinate
            - __id: instance id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a formatted string of the Square instance"""

        s = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
        return s

    @property
    def size(self):
        """Get the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size attribute."""
        self.width = value

    def area(self):
        """Determines area of rectangle instance

        Returns: area
        """
        return super().area()

    def display(self):
        """Prints rectangle instance using its attributes
        with the'#' character.
        """
        return super().display()

    def update(self, *args, **kwargs):
        """Updates attributes of an instance.
        Args:
            - id attribute
            - size attribute
            - x attribute
            - y attribute
        """
        if args is not None and len(args) != 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
