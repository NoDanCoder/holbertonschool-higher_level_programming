#!/usr/bin/python3
""" Import local modules """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class struct """
    def __init__(self, size, x=0, y=0, id=None):
        """ Square class constructor """
        super().__init__(size, size, x, y, id)

# override __str__ metod

    def __str__(self):
        """ modify instance str output """
        return self.f("[{self.getType}] ({self.id}) {self.x}/{self.y} - "
                      "{self.width}")
