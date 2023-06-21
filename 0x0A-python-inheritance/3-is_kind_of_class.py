#!/usr/bin/python3
"""Module contains is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Function that checks whether an object is
    an instance of a class or if the object is an
    instance of a class that inherited from

    Args:
        obj (object): object to be checked
        a_class (class): class pbject to be comapred to obj

    Returns:
        bool: True if obj is an instance of given class or inherited from it
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
