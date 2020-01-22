#!/usr/bin/python3

class Student:
    """ Class Student that defines a Student obj """

    def __init__(self, first_name, last_name, age):
        """ Class Student contructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves Class dict properties """
        return self.__dict__.copy()
