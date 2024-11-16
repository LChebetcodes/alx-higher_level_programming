#!/usr/bin/python3
"""
This module defines the class Rectangle that inherits from
BaseGeometry (7-base_geometry.py)

The class includes:
Instantiation with width and height: def __init__(self, width, height):
width and height must be private. No getter or setter
width and height must be positive integers, validated by integer_validator

"""


class BaseGeometry:
    """
    A base class for geometric shapes.

    Methods:
        area: Raises an exception indicating that it is not implemented.
        integer_validator: Validates that a given value is a positive integer.
    """
    def area(self):
        """Raises an exception since area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is a positive integer."""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Initializes a Rectangle instance with width and height."""
        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height

        # Set width and height as private variables
        self.__width = width
        self.__height = height
