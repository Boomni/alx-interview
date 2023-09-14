#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
def rotate_2d_matrix(matrix):
    """Function that rotates a 2D matrix"""
    reverse = matrix[::-1]
    for index, value in enumerate(reverse):
        matrix.append([item[index] for item in reverse])
    for i in range(len(reverse)):
        del matrix[0]
