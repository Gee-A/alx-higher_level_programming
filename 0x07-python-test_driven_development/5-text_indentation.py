#!/usr/bin/python3

"""
Module contain text_indentation function
"""


def text_indentation(text):
    """
    text_indentation prints a text with 2 new lines after each
    of this characters: '.?:'
    Arg:
        text: a string with no space at the beginning
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)]
        )

    print("{}".format(text), end="")