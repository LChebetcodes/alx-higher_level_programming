#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    obj: The object to introspect.

    Returns:
    list: A list containing the names of the object's attributes and methods.
    """
    return dir(obj)
