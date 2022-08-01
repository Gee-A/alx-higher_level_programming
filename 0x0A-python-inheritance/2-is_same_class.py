#!/usr/bin/python3

"""Module 2-is_same_class.
Contains a method that check if an object is an instance
of the specifed class.
"""


def is_same_class(obj, a_class):
    """Returns True if 'obj' is exactly an instance of 'a_class'
    args:
        obj: object in consideration
        a_class: reference class

    Returns: True if obj is an instance of a_class, False Otherwise
    """
    return True if type(obj) is a_class else False
