#!/usr/bin/python3
def add_integer(a, b=98):
    """Function that adds two integers (or floats) together."""

    """Check if a is an integer or float, and raise a TypeError if not"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    """ Check if b is an integer or float, and raise a TypeError if not"""
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    """Check for NaN and infinity before casting to int"""
    if isinstance(a, float):
        if a != a or a == float('inf') or a == float('-inf'):  # NaN or infinity
            raise TypeError("a must be an integer")

    if isinstance(b, float):
        if b != b or b == float('inf') or b == float('-inf'):  # NaN or infinity
            raise TypeError("b must be an integer")

    """Cast a and b to integers if they are floats"""
    return int(a) + int(b)
