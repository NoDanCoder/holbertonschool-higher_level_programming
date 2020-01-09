#!/usr/bin/python3
class Square:
    """ empty class Square that defines a square """

    def __init__(self, size=0):
        """ inizialize Square class """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        """ return the current square area """

        return self._Square__size ** 2

    @property
    def size(self):
        """ retrieve the size of Square obj """

        return self._Square__size

    @size.setter
    def size(self, value):
        """ set the size of Square obj """

        self.__init__(value)
