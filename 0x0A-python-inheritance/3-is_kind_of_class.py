#!/usr/bin/python3
"""
This module provides the function is_kind_of_class,
which checks if an object is an instance of a specified class or its subclass.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of a_class or an instance of a
    subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class or a subclass of a_class;
        False otherwise.
    """
    return isinstance(obj, a_class)
