#!/usr/bin/python3
"""
module for my lists (inherits from list)
"""


class Mylist(list):
    """
    elements of the list int type
    return my list and sorted list
    """
    def print_sorted(self):
        # sorted method
        # sorted(iterable[, key][, reverse])
        print(sorted(self))
