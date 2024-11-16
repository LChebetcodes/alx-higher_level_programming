#!/usr/bin/python3
"""
This module defines the `BaseGeometry` class, which serves as a foundation
for creating geometric shapes.

The class includes:
    - A placeholder method `area` that raises an exception, indicating
      it must be implemented by subclasses.
    - A method `integer_validator` that validates integer values.
"""


class BaseGeometry:
    """
    A base class for geometric shapes.

    Methods:
        area: Raises an exception indicating that it is not implemented.
        integer_validator: Validates that a given value is a positive integer.
    """

    def integer_validator(self, name, value):
        """
        Validates that the provided value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(name, str):
            raise TypeError(f"{name} must be a string")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """
        Calculates the area of the geometric shape.

        Raises:
            Exception: Always, with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
