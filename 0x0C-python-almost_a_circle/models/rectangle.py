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
        return self.__height

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

# update method

    def update(self, *args):
        """ Update the class Rectangle """
        prop = [self.id, self.width, self.height, self.x, self.y]
        prop[:len(args)] = args
        prop.append(prop.pop(0))
        self.__init__(*prop)

# modifiers methods

    def area(self):
        """ returns the area value of the Rectangle instance """
        return self.width * self.height

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        print("\n" * self.y, end="")
        print("\n".join([" " * self.x + "#" * self.width] * self.height))

# override __str__ metod

    @property
    def getType(self):
        """ retrieves self type """
        return self.__class__.__name__

    def f(self, string):
        """ sumulate f-strings available from python 3.6 """
        return string.format(**locals())

    def __str__(self):
        """ modify instance str output """
        return self.f("[{self.getType}] ({self.id}) {self.x}/{self.y} - "
                      "{self.width}/{self.height}")
