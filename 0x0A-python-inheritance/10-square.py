#!/usr/bin/python3
"""
Module to define the BaseGeometry, Rectangle, and Square classes.
"""


class BaseGeometry:
    """
    Base class for geometry-related classes, providing validation methods.
    """

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
        name (str): The name of the variable.
        value (int): The value to validate.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is not a positive integer.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle instance with width and
        height, which must be positive integers.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

        Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is not a positive integer.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        str: The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    A class representing a square that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes the Square instance with size,
        which must be validated as a positive integer.

        Args:
        size (int): The size of the square.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is not a positive integer.
        """
        self.integer_validator("size", size)  # Validate size using
        # the BaseGeometry method
        self.__width = size
        self.__height = size
        super().__init__(self.__width, self.__height)  # Initialize as a Rectangle with
        # equal width and height

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__width * self.__height  # Use the inherited area() method from Rectangle
