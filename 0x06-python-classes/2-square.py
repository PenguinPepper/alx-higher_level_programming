#!/usr/bin/python3
"""Module contains class that defines a square
"""


class Square:
    ''' Class that defines a square
    '''
    def __init__(self, size=0):
        '''Initialize a variable called size

        Args:
            size (int): Size of the square must be an integer

        Attributes:
            size (int): Size of the square
        '''
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
