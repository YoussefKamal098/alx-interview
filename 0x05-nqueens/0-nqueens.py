#!/usr/bin/python3
"""
Solution to the n-queens puzzle.
The n-queens  puzzle is the problem of placing n
queens on an n x n chessboard such that no two queens attack each other.
This program solves the n-queens problem and returns all unique configurations
for placing n queens on an n x n chessboard.
Each configuration is represented as a list of positions where queens are
placed, with each position specified by (row, col) coordinates.
The program takes a single argument N, which is the size of the board.
The program prints all possible solutions to the problem,
one solution per line. The solutions are printed in lexicographical order,
with the rows sorted in ascending order and the columns sorted from
left to right. The program usage is as follows: nqueens N where N is
the size of the board. The program exits with the status code 1 if the
user does not provide the correct number of arguments or if N is less than 4.
The program is written in Python 3.8 and uses the sys module to
access command-line arguments.
The program is executed as follows:
./0-nqueens.py N where N is the size of the board.
The program is tested using the following command: ./0-nqueens.py 4
"""
import sys


def solve_nqueens(n):
    """
    Solves the N-Queens problem and returns all unique configurations
    for placing N queens on an N x N chessboard.

    Each configuration is represented as a list of positions where
    queens are placed, with each position specified by
    (row, col) coordinates.
    """
    columns = set()
    positive_diagonals = set()
    negative_diagonals = set()

    def can_place_queen(row, col):
        """Check if a queen can be placed at the given (row, col) position."""
        return (col not in columns and
                (row + col) not in positive_diagonals and
                (row - col) not in negative_diagonals)

    def place_queens(row):
        """
        Recursively attempt to place queens on the board starting from
        the given row. Returns a list of possible placements for
        each subsequent row.
        """
        if row == n:
            return [[]]

        solutions = []

        for col in range(n):
            # Check if queen can be placed at this position
            if not can_place_queen(row, col):
                continue

            # Place queen and mark attacked columns and diagonals
            columns.add(col)
            positive_diagonals.add(row + col)
            negative_diagonals.add(row - col)

            # Recur to next row
            for placement in place_queens(row + 1):
                solutions.append(placement + [[row, col]])

            # Remove queen and clean up attacked columns and diagonals
            columns.remove(col)
            positive_diagonals.remove(row + col)
            negative_diagonals.remove(row - col)

        return solutions

    return place_queens(0)


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

    for solution in solve_nqueens(n):
        print(solution)
