#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n

    Args:
        n: integer

    Return:
        Empty list if n <= 0 else list of lists of integers.
    """
    if n < 1:
        return []

    triangle = []

    for row_number in range(n):
        current_row = []
        current_row.append(1)

        for i in range(1, row_number):
            first_num = triangle[row_number - 1][i - 1]
            second_num = triangle[row_number - 1][i]
            summation = first_num + second_num
            current_row.append(summation)

        if row_number > 0:
            current_row.append(1)

        triangle.append(current_row)

    return triangle
