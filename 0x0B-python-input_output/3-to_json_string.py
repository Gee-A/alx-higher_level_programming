#!/usr/bin/python3

"""Module 3-to_json_string
Returns the JSON representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of my_obj
    Args:
        my_obj: string to represent
    Returns: JSON representation
    """
    return json.dumps(my_obj)
