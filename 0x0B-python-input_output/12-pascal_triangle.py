#!/usr/bin/python3

"""Module 12-pascal_triangle
Returns a list of lists of integers
representing the Pascal's triangle of n.
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.
    Args:
        - n: size of the triangle (rows)
    Returns: a list of list of integers
    """

    if n <= 0:
        return []

    table = [[0 for x in range(i + 1)] for i in range(n)]
    table[0] = [1]

    for row in range(1, n):
        table[row][0] = 1
        for col in range(1, row + 1):
            if col < len(table[row - 1]):
                table[row][col] = table[row - 1][col - 1] + table[row - 1][col]
            else:
                table[row][col] = 1
    return table
