#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Function that rotates a 2D matrix"""
    length = len(matrix)
    reverse = matrix[::-1]
    matrix.clear()
    for index in range(length):
        matrix.append([item[index] for item in reverse])
