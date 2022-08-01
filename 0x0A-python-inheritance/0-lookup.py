#!/usr/bin/python3

"""Module 0-lookup.
contains a lookup function that takes obj and return list of
available attributes and method
"""


def lookup(obj):
    """Returns a list of available attributes and methods

    Args:
        obj: objec to look into
    """
    return dir(obj)
