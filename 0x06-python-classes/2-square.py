#!/usr/bin/python3
'''
Module of a Square class
'''


class Square:
    '''A simple calss that defies a square
    Attributes:
        size: The size of the square
    '''

    def __init__(self, s ize=0):
        '''Initialzaton mehtod for the Square class
        Args:
            size(int): The size of the square
        '''
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            rasie TypeError("size must be an integer")
