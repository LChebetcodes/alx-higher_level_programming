#!/usr/bin/python3
"""
This module provides a function  that writes a string to a text file"""
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
