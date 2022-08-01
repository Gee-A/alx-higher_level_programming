#!/usr/bin/python3

"""Module 4-inherits_from.
Determines if an object inherited from a specified class
"""


def inherits_from(obj, a_class):
    """Check if obj inherits directly/indirectly from a specified class
    Args:
        obj: object in consideration
        a_class: reference class

    Returns: True (if title is satisfied)
    False (Otherwise)
    """
    return isinstance(obj, a_class) and type(obj) != a_class
