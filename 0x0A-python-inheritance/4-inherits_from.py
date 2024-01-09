#!/usr/bin/python3
"""
Module to check if object is an instance of a
class that inherited (directly or indirectly)
from the specified class
"""


def inherits_from(obj, a_class):
        
"""
    Checks if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check inheritance from.

    Returns:
        True if the object inherits from the class, False otherwise.
    """

    if isinstance(obj, a_class):
        return True

    cls = obj.__class__
    while cls is not None:
        if cls is a_class:
            return True
        cls = cls.__base__

    return False
