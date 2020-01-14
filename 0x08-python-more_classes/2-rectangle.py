#!/usr/bin/python3
class Rectangle:
    """ class Rectangle that defines a rectangle """

# inizialise instance

    def __init__(self, width=0, height=0):
        """ set properties to instance """
        self.height = height
        self.width = width

    def __testInput(self, prop, value):
        """ test width and heigh inputs """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(prop))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(prop))
        return True

    @property
    def width(self):
        """ width getter """
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """ width setter """
        if self.__testInput("width", value):
            self._Rectangle__width = value

    @property
    def height(self):
        """ height getter """
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """ height setter """
        if self.__testInput("height", value):
            self._Rectangle__height = value

# get area and perimeter

    def area(self):
        """ set area of Rectangule instance """
        return self.width * self.height

    def perimeter(self):
        """ set perimeter of Rectangule instance """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
