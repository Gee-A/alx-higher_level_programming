#!/usr/bin/python3

"""
say_my_name prints the entered names on a line and return
the appropriate error message if any is not string
"""


def say_my_name(first_name, last_name=""):
    """
    Prints <first_name> <last_name>
    Args:
        first_name: string type
        second_name: string type
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
