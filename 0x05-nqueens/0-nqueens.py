#!/usr/bin/python3
"""N queens"""

import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at the specified row and col."""
    for i in range(col):
        if (board[i] == row or
                board[i] - i == row - col or
                board[i] + i == row + col):
            return False
    return True


def solve_nqueens(n, board, col):
    """Use backtracking to solve N queens problem."""
    if col >= n:
        print([[i, board[i]] for i in range(n)])
        return

    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i
            solve_nqueens(n, board, col + 1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1 for _ in range(n)]
    solve_nqueens(n, board, 0)
