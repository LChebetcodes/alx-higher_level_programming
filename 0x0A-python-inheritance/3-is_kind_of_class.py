#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class or a subclass thereof.

    Parameters:
    obj: The object to check.
    a_class: The class to compare the object against.
    """
    return isinstance(obj, a_class)
    """Returns:
    bool: True if obj is an instance of a_class
            or a class that inherited from a_class, False otherwise."""
