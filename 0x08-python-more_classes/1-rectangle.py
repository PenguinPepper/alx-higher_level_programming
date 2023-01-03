#!/usr/bin/python3
'''This module contains a class called Rectangle'''


class Rectangle:
    '''class Rectangle that defines a rectangle'''

    def __init__(self, width=0, height=0):
        '''Initialises height and width of Rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        '''
        self.__height = height
        self.__width = width

    @property
    def height(self):
        '''Get & set heigh of rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        '''Get and set width of rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
