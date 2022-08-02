#!/usr/bin/python3

"""Module 9-student.py
Creates a Student class."""


class Student:
    """Defines a student
    Public attributes:
        - first_name
        - last_name
        - age
    Public method: to_json()
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a student instance"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance.

        Returns: the dict representation of the instance.
        """
        return self.__dict__
