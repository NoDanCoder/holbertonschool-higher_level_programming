#!/usr/bin/python3
""" import JSON representation """
import json
import csv
from inspect import signature as sg
from os.path import isfile
import turtle
from random import randint


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

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        parameters = [k for k, v in dict(sg(cls).parameters).items()]
        dum = cls(*[1 for x in parameters if str(sg(cls).parameters[x]) == x])
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances writen in JSON """
        inpFile = cls.__name__ + ".json"
        if isfile(inpFile):
            with open(inpFile, "r", encoding="utf-8") as f:
                buff = cls.from_json_string(f.read())
                return [cls.create(**x) for x in buff]
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ convert obj into csv data """
        outFile = cls.__name__ + ".csv"
        list_objs = [x.to_dictionary() for x in list_objs] if list_objs else []
        with open(outFile, "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=[x for x in list_objs[0].keys()])
            writer.writeheader()
            [writer.writerow(x) for x in list_objs]

    @classmethod
    def load_from_file_csv(cls):
        """ load csv file """
        inpFile = cls.__name__ + ".csv"
        if isfile(inpFile):
            with open(inpFile, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                reader = [{k: int(v) for k, v in dict(x).items()} for x in reader]
                return [cls.create(**x) for x in reader]

# draw turtle

    @staticmethod
    def makeDraw(dictObj, obj):
        """ make a draw of instance in turtle """
        tim = turtle.Turtle()
        tim.width(5)
        tim.color("#%06x" % randint(0, 0xFFFFFF))
        tim.penup()
        tim.goto(dictObj["x"], dictObj["y"])
        tim.pendown()
        tim.begin_fill()
        if obj is "Squ":
            for i in range(4):
                tim.forward(dictObj["size"])
                tim.right(90)
        elif obj is "Rect":
            for i in range(2):
                tim.forward(dictObj["width"])
                tim.right(90)
                tim.forward(dictObj["height"])
                tim.right(90)
        tim.end_fill()

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ opens a window and draws all the Rectangles and Squares """
        list_rectangles = [x.to_dictionary() for x in list_rectangles] if list_rectangles else []
        list_squares = [x.to_dictionary() for x in list_squares] if list_squares else []
        for x in list_rectangles:
            Base.makeDraw(x, "Rect")
        for x in list_squares:
            Base.makeDraw(x, "Squ")
        turtle.done()
