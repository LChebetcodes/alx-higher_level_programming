#!/usr/bin/python3
"""
Module for adding a new attribute to an object.

This module defines a function `add_attribute`
that adds a new attribute to an object
if it is possible.
If the object cannot accept new attributes, a `TypeError` is raised.
"""


def add_attribute(obj, attr_name, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj (object): The object to which the attribute will be added.
        attr_name (str): The name of the attribute to add.
        value (any): The value of the new attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, value)
