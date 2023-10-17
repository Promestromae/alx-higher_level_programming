#!/usr/bin/python3
""" This Module that defines the class Student
"""


class Student:
    """ Class to represent student instances """

    def __init__(self, first_name, last_name, age):
        """ define special method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Method that returns specified directory description """
        return self.__dict__.copy()
