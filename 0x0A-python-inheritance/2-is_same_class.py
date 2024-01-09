#!/usr/bin/python3
"""
module that contains function to check if an object
is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    object is the most base type class, a_class
    contain instance of the object class
    """
    # class type(object)
    if (type(obj) == a_class):
        # the object is exactly an instance of the a_class
        return True
    # otherwise,
    return False
