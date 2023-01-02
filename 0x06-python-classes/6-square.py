#!/usr/bin/python3
'''Module contains a class called square'''


class Square:
    '''Square class with size and psotion attribute and 2 methods'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialises size and position of square'''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''Gets the size of the square

        @size.setter:
            value: ensures that the value entered is an int and is > 0
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

    @property
    def position(self):
        '''position: tuple of two positive integers

        @position.setter:
            value: cheks that two positive integers are entered
        '''
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or value[0] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        '''Calculates Area of square

        Returns:
            Area of square
        '''
        return self.__size ** 2

    def my_print(self):
        '''Method to print the square using #'''
        if self.__size > 0:
            for i in range(self.__position[1]):
                print("")
            for j in range(1, self.__size + 1):
                print("{}{}".format(' ' * self.__position[0], '#'*self.__size))
        else:
            print('')
