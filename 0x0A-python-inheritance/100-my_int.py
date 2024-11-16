#!/usr/bin/python3
"""
This module defines the MyInt class, a subclass of int
that inverts the behavior of the equality (==) and inequality (!=) operators.

Classes:
    MyInt: A rebellious integer class that swaps the functionality of
           equality and inequality operators.
"""


class MyInt(int):
    """
    A rebellious integer class that inherits from int but inverts the
    functionality of the equality and inequality operators.

    Attributes:
        None
    """

    def __eq__(self, other):
        """
        Overrides the equality operator.

        Args:
            other (any): The object to compare with.

        Returns:
            bool: False if the values are equal, True otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator.

        Args:
            other (any): The object to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
