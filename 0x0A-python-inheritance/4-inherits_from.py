#!/usr/bin/python3
"""
This module provides the function inherits_from,
which checks if the object
is an instance of a class that inherited (directly or indirectly)
from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Determines if an object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class. Excludes instances of the specified class itself.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj is an instance of a subclass
        of a_class (but not a_class itself),
        False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
