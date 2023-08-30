#!/usr/bin/env python3
"""N queens"""
import sys


def is_valid(board, row, col):
    """Checks if board is valid"""
    for prev_row in range(row):
        if board[prev_row] == col or \
           abs(board[prev_row] - col) == abs(prev_row - row):
            return False
    return True


def solve_n_queens(n):
    """Solver"""
    def backtrack(row):
        """Backtracker"""
        nonlocal solutions
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1)

    solutions = []
    board = [-1] * n
    backtrack(0)

    for solution in solutions:
        print([[i, j] for i, j in enumerate(solution)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        solve_n_queens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
