#!/usr/bin/python3
"""
This module defines a class Square with a private instance
attribute size and the corresponding property and setter method as used here
"""


class Square:
    """
    This class represents a class square with a private instance attribute
    size and the corresponding property setter methods"""

    def __init__(self, size=0):
        """This method instantializes the square with the given size"""
        self.size = size

    @property
    def size(self):
        """This method returns the size of the instantiated square"""
        return self.__size

    @size.setter
    def size(self, value):
        """This method sets the size of the given square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method returns the are of the current square"""
        return self.__size ** 2

    def my_print(self):
        """This method prints the square with the character # in stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
