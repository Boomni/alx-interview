#!/usr/bin/python3
"""
0-pascal_triangle.py
"""

def pascal_triangle(n):
    if n < 1:
        return []

    triangle = []

    for row_number in range(n):
        current_row = []
        current_row.append(1);

        for i in range(1, row_number):
            value = triangle[row_number - 1][i - 1] + triangle[row_number - 1][i]
            current_row.append(value)

        if row_number > 0:
            current_row.append(1)

        triangle.append(current_row)

    return triangle
