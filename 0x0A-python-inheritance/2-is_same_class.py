#!/usr.bin/python3
"""Module contains is_same_class"""


def is_same_class(obj, a_class):
    """Function tat checks whether an onbject is
    exactly an instance of a class or not
 
    Args:
        obj (object): object to be checked
        a_class (class): class pbject to be comapred to obj

    Returns:
        bool: True if obj is an instance of given class
    """
    if type(obj) is a_class:
        return True
