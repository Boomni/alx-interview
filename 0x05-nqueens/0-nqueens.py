#!/usr/bin/python3
"""N-queens"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N\n")
    exit(1)
try:
    integer = int(sys.argv[1])
except TypeError:
    print("N must be a number\n")
    exit(1)
if integer < 4:
    print("N must be at least 4\n")
    exit(1)
