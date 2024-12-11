#!/usr/bin/python3
"""
This module provides a function  that  writes an Object to a text file
"""

import json


def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The corresponding Python object.
    """
    return json.loads(my_str)


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a file using JSON representation.

    Args:
        my_obj (object): The object to serialize.
        filename (str): The file name to save the JSON content.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
