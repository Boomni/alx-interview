#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
def rotate_2d_matrix(matrix):
    matrix.reverse()
    copy = matrix
    new = []
    for index, row in matrix.:
        new.append([num[index] for num in copy])
if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
