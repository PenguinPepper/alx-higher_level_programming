#!/usr/bin/python3
'''This module contains a class called Rectangle'''


class Rectangle:
    '''class Rectangle that defines a rectangle'''

    def __init__(self, width=0, height=0):
        '''Initialises height and width of Rectangle

        Args:
            width(int): width of rectangle
            height(int): height of rectangle
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''width: returns the width of rectangle

        @width.setter:
            value: ensures width is > 0 and an integer
        '''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        '''height: returns the height of the square

        @height.setter:
            value: ensures that height > 0 and is an integer
        '''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
