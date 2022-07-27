#!/usr/bin/python3
"""Module add_integer adds two numbers to return an integer"""


def add_integer(a, b=98):
    """
    Return the addition of a and b, or error
    if a or b is not of int or float type.
    Args:
        a: first number
        b: second number
    """

    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")

    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
