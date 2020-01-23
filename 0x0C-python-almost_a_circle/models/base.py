#!/usr/bin/python3
class Base:
    """ Base class struct """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Base class constructor """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
