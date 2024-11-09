#!/usr/bin/python3
"""
A simple module that that multiplies 2 matrices.
"""


def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices"""
    """Validate that m_a and m_b are lists"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    """Validate that m_a and m_b are lists of lists"""
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    """Check if m_a or m_b are empty"""
    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty"
        if len(m_a) == 0 else "m_b can't be empty")
        for row in m_a:
            if not all(isinstance(elm, (int, float)) for elm in row):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(elm, (int, float)) for elm in row):
            raise TypeError("m_b should contain only integers or floats")

    row_len_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_len_a:
            raise TypeError("each row of m_a must be of the same size")

    row_len_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_len_b:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            row_result.append(sum(m_a[i][k] * m_b[k][j]
            for k in range(len(m_b))))
        result.append(row_result)

    return result
