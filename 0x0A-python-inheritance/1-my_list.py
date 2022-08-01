#!/usr/bin/python3

"""Module 1-my_list.
Contains MyList class that extending the list function.
"""


class MyList(list):
    """My List inherits from List."""

    def print_sorted(self):
        """Prints a sorted list in ascending order."""
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
