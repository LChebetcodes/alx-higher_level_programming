#!/usr/bin/python3
"""
A simple module that that divides all elements of a matrix.
"""


def text_indentation(text):
    """Function that adds two integers (or floats) together."""
    """Check if text is a string"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    """Initialize the current position in the text"""
    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:
            print(text[i], end="")
            print()
            print()
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        else:
            print(text[i], end="")
        i += 1
