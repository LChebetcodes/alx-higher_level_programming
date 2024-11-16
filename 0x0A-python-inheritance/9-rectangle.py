#!/usr/bin/python3
"""
Module to define the BaseGeometry class and
Rectangle class that inherits from BaseGeometry.
This module includes the necessary validation and
area calculation for the Rectangle class.
"""


class BaseGeometry:
    """
    A base class for geometric objects.
    It provides methods that can be used by other geometric shapes.
    """

    def area(self):
        """
        Raises an exception if the area method
        is not implemented in a subclass.
        This is meant to be overridden by subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the provided value is a positive integer.

        Args:
        name (str): The name of the variable to be used in error messages.
        value (int): The value to be validated.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle that inherits from BaseGeometry.
    This class validates the width and height, calculates the area,
    and formats the description of the rectangle.

    Attributes:
    __width (int): The width of the rectangle.
    __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle instance with width and height,
        both validated as positive integers.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

        Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is not a positive integer.
        """
        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height
        self.__width = width  # Store width as a private attribute
        self.__height = height  # Store height as a private attribute

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle in the format:
        [Rectangle] <width>/<height>

        Returns:
        str: The formatted string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
