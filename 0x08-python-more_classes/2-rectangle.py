#!/usr/bin/python3
'''Module contains a class called Rectangle'''


class Rectangle:
    '''class Rectangle that defines a rectangle

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
    '''

    def __init__(self, width=0, height=0):
        '''Initialises width and height

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        '''
        self.__height = height
        self.__width = width

    @property
    def width(self):
        '''Get and set width of rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''Get & set height'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''Calculates area of rectangle

        Returns:
            width * height
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''Calculates perimeter

        Returns:
            width + height
        '''
        if self.__height == 0:
            return 0
        if self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2
