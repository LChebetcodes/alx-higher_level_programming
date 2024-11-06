#!/usr/bin/python3
"""
A simple module that adds two integers.
"""

def add_integer(a, b=98):  
    """
    Adds two integers or floats (casting floats to integers).
    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float, defualt is 98.

    Returns:
        int: The sum of a and b as integers.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    """Cast to integers before adding"""
    return int(a) + int(b)
