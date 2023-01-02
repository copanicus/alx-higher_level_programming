#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    def is_safe(board, row, col):
        """Check if it is safe o place a quee at board[row][col].

        Check if there is a queen in the same column

        """
        for i in range(row):
            if board[i][col] == 1:
                return False

        """Check upper left diagonal"""
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        """Check upper right diagonal"""
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1
        return True

    def solve(board, row):
        if row == n:
            """All queen have been well place"""
            print(board)
            return True

        for col in range(n):
            if is_safe(board, row, col):
                """Place queen at board[row][col]"""
                board[row][col] = 1
                """Recurseively place the rest of the queens"""
                if solve(board, row + 1):
                    return True
                """Backtrack: remove queen from board[row][col]"""
                board[row][col] = 0

        return False

    """Initialize empty board"""
    board = [[0] * n for _ in range(n)]
    solve(board, 0)

def main():
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

    nqueens(n)

if __name__ == "__main__":
    main()
