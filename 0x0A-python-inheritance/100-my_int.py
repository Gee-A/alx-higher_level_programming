#!/usr/bin/python3

"""Module 100-my_int
MyInt inherits from int"""


class MyInt(int):
    """MyInt defines == and != operations
    but reverses them.
    Inherit: int
    """

    def __eq__(self, other):
        """Equality becomes inequality."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inequality becomes equality."""
        return super().__eq__(other)
