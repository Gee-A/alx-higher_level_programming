#!/usr/bin/python3

"""Module 7-add_item
Add all arguments to a Python list and save them to a file."""

import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    my_file = "add_item.json"

    try:
        my_list = load_from_json_file(my_file)
    except FileNotFoundError:
        my_list = []
    for arg in sys.argv[1:]:
        my_list.append(arg)

    save_to_json_file(my_list, my_file)
