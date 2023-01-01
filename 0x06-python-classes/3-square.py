#!/usr/bin/python3
'''Module contains a class called Square'''


class Square:
    '''This class contain the attributes to a square'''
    def __init__(self, size=0):
        '''Initialises the size variable for the object.

        Args:
            size (int): size of the quare, must be greater than 0.
        '''
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        '''Method determines the area of the square.

        Returns:
            The area of the square.
        '''
        return self.__size**2
