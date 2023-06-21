#!/usr/bin/python3
"""Module contains inherits_from"""


def inherits_from(obj, a_class):
    """Function that checks whether an object is
    an instance of a class or if the object is an
    instance of a class that inherited from

    Args:
        obj (object): object to be checked
        a_class (class): class pbject to be comapred to obj

    Returns:
        bool: True if obj is an instance of given class or inherited from it
    """
    what_i_am = type(obj)
    if isinstance(what_i_am, a_class):
        return True
    else:
        return False
