#!/usr/bin/python3
"""
This module provides a function to read
a text file (UTF-8) and print its contents to stdout.
"""


def read_file(filename=""):
    """
    Reads a UTF8 text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.
        Default is an empty string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
