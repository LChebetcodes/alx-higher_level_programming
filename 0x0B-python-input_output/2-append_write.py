#!/usr/bin/python3
"""
This module provides a function  that writes a string to a text file"""

def append_write(filename="", text=""):
    """Appends a string to a text file (UTF-8) and returns the number of characters added."""
    with open(filename, "a", encoding="utf-8") as file:
        chars_written = file.write(text)
    return chars_written
