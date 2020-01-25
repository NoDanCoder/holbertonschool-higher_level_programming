#!/usr/bin/python3
""" import JSON representation """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of 'list_dictionaries' """
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"
