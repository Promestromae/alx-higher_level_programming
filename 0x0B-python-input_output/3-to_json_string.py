#!/usr/bin/python3
"""func to_json_string
Returns the JSON representation of an object(string)
"""
import json


def to_json_string(my_obj):
    """ Function that returns the JSON representation of an object

    Args:
        my_obj: object to return

    Returns:
        my_obj: a json object rep

    """
    return json.dumps(my_obj)
