#!/usr/bin/python3
"""
A simple module that that divides all elements of a matrix.
"""


def say_my_name(first_name, last_name=""):
    """Check if first_name is a string"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    """Check if last_name is a string"""
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    """Print the name"""
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
