#!/usr/bin/python3
""" import local modules """
from models.base import Base

class Rectangle(Base):
    """ Rectangle class struct """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle class constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def checkInp(name, value, compare):
        """ check if inp fit to class properties """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if not eval("value {} 0".format(compare)):
            raise ValueError("{} must be {} 0".format(name, compare))

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        self.checkInp("width", value, ">")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__width

    @height.setter
    def height(self, value):
        """ height setter """
        self.checkInp("height", value, ">")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        self.checkInp("x", value, ">=")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        self.checkInp("y", value, ">=")
        self.__y = value
