#!/usr/bin/Python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for num in range(0, x):
        try:
            print("{:d}".format(my_list[num]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
