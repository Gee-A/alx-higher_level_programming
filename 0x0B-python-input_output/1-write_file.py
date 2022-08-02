#!/usr/bin/python3

"""Module 1-write_file
Writes a string to a text file"""


def write_file(filename="", text=""):
    """Write 'text' into 'filename'
    Args:
        filename: name of file to write to
        text: content to write in the file

    Return: number of characters written
    """
    with open(filename, 'w') as f:
        return f.write(text)
