#!/usr/bin/python3

"""Module 3-is_kind_of_class.
Determines if an object is a kind of a specified class.
"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or the class its super class

    Args:
        obj: object in consideration
        a_clas: reference class

    Returns: True (If title is satisfied)
    False (Otherwise)
    """
    return isinstance(obj, a_class)
