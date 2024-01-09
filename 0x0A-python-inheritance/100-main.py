#!/usr/bin/python3
"""
class MyInt that inherits from int
"""


class MyInt(int):
    """
    A rebellious subclass of int with inverted comparison operators.
    """

    def __eq__(self, other):
        """
        Inverts the == operator to return True if values are not equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator to return True if values are equal.
        """
        return super().__eq__(other)

