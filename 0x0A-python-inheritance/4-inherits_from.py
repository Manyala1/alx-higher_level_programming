#!/usr/bin/python3
"""
Module to check if an instance of a class that inherited (directly or idirectly)
from the specified class 
"""


def inherits_from(obj, a_class):
    """
    True if object is an instance of a classthat inherited
    (directlt/indirectly) from the specified class
    """
    if type(obj) == a_class:
        return False
    return isintance(obj, a_class)
