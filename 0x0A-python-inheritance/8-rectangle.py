#!/usr/bin/python3
#!/usr/bin/python3
"""
This module defines the class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
"""


class BaseGeometry:
    """
    A BaseGeometry class to define common geometric operations.
    """
    def area(self):
        """
        Raises an exception since area is not implemented in the base class.

        This method must be implemented by subclasses.
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to zero.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A Rectangle class that inherits from BaseGeometry.

    This class defines a rectangle with specific width and height, both of which
    must be positive integers. The rectangle also supports calculating its area.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height):
            Initializes a Rectangle instance with the given width and height.
        area(self):
            Returns the area of the rectangle (width * height).
    """
    
    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with the provided width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Validates that both width and height are positive integers using the
        integer_validator method from the BaseGeometry class.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to zero.
        """
        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height
        
        # Set width and height as private variables
        self.__width = width
        self.__height = height
