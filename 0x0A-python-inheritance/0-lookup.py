#!/usr/bin/python3
"""
This module provides the function lookup,
which returns a list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of attribute and method names available for obj.
    """
    return dir(obj)
