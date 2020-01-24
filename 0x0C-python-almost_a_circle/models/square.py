#!/usr/bin/python3
""" Import local modules """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class struct """
    def __init__(self, size, x=0, y=0, id=None):
        """ Square class constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

# override __str__ metod

    def __str__(self):
        """ modify instance str output """
        return self.f("[{self.getType}] ({self.id}) {self.x}/{self.y} - "
                      "{self.width}")

# get properties

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        dic = super().to_dictionary()
        dic.update({"size": self.size})
        return {k:v for k, v in dic.items() if k not in ["width", "height"]}
