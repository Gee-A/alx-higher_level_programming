#!/usr/bin/Python3

def safe_print_division(a, b):
    try:
        return "{:d}".format(a/b)
    except (ZeroDivisionError, TypeError):
        return "None"
