#!/usr/bin/python3
'''Module contains the class Square'''


class Square:
    '''Class called Square sets size and returns areaof square'''

    def __init__(self, size=0):
        '''Initialises the size of the square

        Args:
            size(int): Size of the square must be greater than o
        '''
        self.__size = size

    @property
    def size(self):
        '''size: the size of the square

        size.setter:
            value: checks the data entered to size if its > 0
            and size is an integer.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        '''Calulates the area of the square'''
        return self.__size ** 2
