#!/usr/bin/python3
"""
A simple module that that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Check if the matrix is a list of lists"""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    """Check if all elements in the matrix are either integers or floats"""
    for row in matrix:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    """Check if each row has the same size"""
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    """Check if div is a number (either integer or float)"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    """Check if div is zero"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    """Perform division, rounding to 2 decimal places"""
    result = []
    for row in matrix:
        result.append([round(i / div, 2) for i in row])
    
    return result
