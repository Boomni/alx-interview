#!/usr/bin/python3
"""Island Perimeter"""

def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""

    squares = 0

    for lists in grid:
        for square in lists:
            if square == 1:
                squares += 1
    return 2 * (1 + squares)
