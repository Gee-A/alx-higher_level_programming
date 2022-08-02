#!/usr/bin/python3

"""Module 0-read_file
Contains a function that reads a text file and prints to stdout
"""


def read_file(filename=""):
    """Reads from filename (UTF8) and prints to stdout
    Args:
        filename: name of file to be read
    """

    with open(filename) as f:
        read_file = f.read()
        print(read_file, end="")
