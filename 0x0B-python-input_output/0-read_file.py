#!/usr/bin/python3

"""Module 0-read_file
Contains a function that reads a text file and prints to stdout
"""


def read_file(filename=""):
    """Reads a text file(UTF8) and prints to stdout
    Args:
        filename: name of file to be read
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read())
