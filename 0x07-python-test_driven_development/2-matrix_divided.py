#!/usr/bin/python3

"""module matrix_divided takes a matrix and div.
   all value in the matrix is divided by div
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix whose element(to 2dp) have been divided by div.
    Args:
        matrix: matrix containing int or float element in row and col
        div: an int or float value
    """

    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not isinstance(matrix[0], list)):
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    count = len(matrix[0])
    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

        for elem in row:
            if not isinstance(elem, int) and not isinstance(elem, float):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

        if count != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
