#!/usr/bin/python3
'''Module contains a class caledd Square'''


class Square:
    '''Square class with size field and 2 methods area and my_print'''

    def __init__(self, size=0):
        '''Initialises the size of square'''
        self.__size = size

    @property
    def size(self):
        '''size: size of the square

        size.setter:
            value: makes sure size is > 0 and an integer
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
        '''Clultaes the Area of a square

        Returns:
            Area of square
        '''
        return self.__size ** 2

    def my_print(self):
        '''Method that prints the square using #'''
        if self.__size > 0:
            for i in range(1, self.__size + 1):
                print("#" * self.__size)
        else:
            print('')
