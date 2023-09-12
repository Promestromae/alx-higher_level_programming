#!/usr/bin/python3
"""This module creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """ Function creates an Object from a JSON file

    Args:
        filename: textfile name

    Returns:
        obj: with contents

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
