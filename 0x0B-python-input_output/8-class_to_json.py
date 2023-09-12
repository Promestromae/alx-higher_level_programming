#!/usr/bin/python3
""" Module that returns the dictionary description with a simple
data structure for a JSON serialization of an object
"""


def class_to_json(obj):
    """Creates a dictionary description of obj

    Args:
        - obj: object 
    Returns: dictionary description of obj
    """

    return obj.__dict__
