#!/usr/bin/python-3

import sys


def is_safe(board, row, col):
    """Check if there's a queen in the same column"""
    for i in range(row):
        if board[i] == col:
            return False
    """Check upper left diagonal"""
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False
    """Check upper right diagonal"""
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i] == j:
            return False
    return True


def solve_nqueens(board, row, solutions):
    if row == len(board):
        """One solution found, add to the solutions list"""
        solutions.append([[i, board[i]] for i in range(len(board))])
        return
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, solutions)
            board[row] = -1
            """Reset row for backtracking"""


def nqueens(N):
    board = [-1] * N
    solutions = []
    solve_nqueens(board, 0, solutions)
    return solutions


def main():
    """Check the command line arguments"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = nqueens(N)
    for solution in solutions:
        print(solution)
