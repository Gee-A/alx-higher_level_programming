#!/usr/bin/python3

"""Module 2-append_write
Appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Append 'text' into 'filename'
    Args:
        filename: name of file to write to
        text: content to be appended into file

    Return: number of characters appended
    """
    with open(filename, 'a') as f:
        return f.write(text)
