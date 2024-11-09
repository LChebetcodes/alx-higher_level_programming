#!/usr/bin/python3
"""
A simple module that that prints a square with the character #."""


def print_square(size):
    """Check if size is an integer"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    """Check if size is non-negative"""
    if size < 0:
        raise ValueError("size must be >= 0")

    """Print the square"""
    for _ in range(size):
        print("#" * size)
