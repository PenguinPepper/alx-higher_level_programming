#!/usr/bin/python3
'''Module Declares a function called lookup'''


def lookup(obj):
    '''lookup will returns the list of available
    attributes and methods of an object.

    Args:
        obj (object): Object to be searched

    Returns:
        some_list: List of aribes and methods of object
    '''
    some_list = dir(obj)
    return some_list
