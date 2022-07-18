#!/usr/bin/Python3

def safe_print_division(a, b):
    try:
        res = a / b
    except (TypeError, ZeroDivisionError, FloatingPointError):
        res = "None"
    finally:
        print(f"Inside result: {res}")
    return res
