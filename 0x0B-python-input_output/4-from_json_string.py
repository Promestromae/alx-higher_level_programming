#!/usr/bin/python3
"""funct save_to_json_file
Writes an object to a text file using a JSON representation
"""
import json


def from_json_string(my_str):
    """ Function that returns an object by a JSON rep

    Args:
        my_str: JSON representation of the obj data

    Returns:
        my_str: return the json str

    """
    return json.loads(my_str)
