#!/usr/bin/pythonn3
'''Module contains a class called Rectangle'''


class Rectangle:
    '''class Rectangle that defines a rectangle by'''

    def __init__(self, width=0, height=0):
        '''Assigns witdh and height of instane'''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Get and set width of rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        '''Get and set height of rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        '''Calculate the area of a rectancle

        Returns:
            width * height
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''Calculate the perimeter of a rectangle

        Returns:
            perimeter of a rectangle
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        string = ""
        for i in range(self.__height):
            if i < self.__height - 1:
                string += str('#'*self.__width) + '\n'
            else:
                string += str('#'*self.__width)
        return string

    def __repr__(self):
        string_2 = "Rectangle\("
        string_3 = str(self.__width) + str(self.__height)
        string_4 = string_2 = string_3 + "\)"
        return "Rectangle" + string_3
