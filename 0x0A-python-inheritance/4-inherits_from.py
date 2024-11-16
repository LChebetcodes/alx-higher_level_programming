#!/usr/bin/python3
"""
This module defines the function `inherits_from` which determines if an object
is an instance of a class that inherited (directly or indirectly) from a
specified class, excluding instances of the class itself.
"""


def inherits_from(obj, a_class):
    """
    Determines if an object is an instance of a class that inherited (directly
    or indirectly) from the specified class.
    Excludes instances of the specified class itself.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj is an instance of a subclass of
        a_class (but not a_class itself), False otherwise.

    Examples:
        >>> class A:
        ...     pass
        >>> class B(A):
        ...     pass
        >>> a = A()
        >>> b = B()
        >>> inherits_from(a, A)
        False
        >>> inherits_from(b, A)
        True
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
