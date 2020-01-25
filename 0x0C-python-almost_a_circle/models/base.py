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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        outFile = cls.__name__ + ".json"
        list_objs = [x.to_dictionary() for x in list_objs] if list_objs else []
        with open(outFile, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        return json.loads(json_string) if json_string else []
