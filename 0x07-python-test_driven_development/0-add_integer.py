#!/usr/bin/python3
'''This module contains a dunction called add_integer'''
def add_integer(a, b=98):
    '''Function that adds two integers a and b

    Args:
        a (int): can be an integer or a float
        b (int): can be an integer or float 

    Returns:
        The addition of a and b as an int type
    '''
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    else:
        a = int(a)
        b = int(b)
    return a + b
