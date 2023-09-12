#!/usr/bin/python3
"""This module defines a text file-reading function
def read_file(filename=""):
    """ Function that reads from a utf-8 file

    Args:
        filename: filename

    Raises
        Exception: when the file cannot be opened

    """

    with open(filename, 'r', encoding="utf-8") as f:
        contents = f.read()
        print(contents, end="")
