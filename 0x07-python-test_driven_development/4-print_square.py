# (remove this)!/usr/bin/python3

"""module contain print_square function that prints a sqaure base on size"""


def print_square(size):
    """
    print_square module prints a square with the character #
    Args:
        size: a positive integer value
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)