# N Queens Problem

## Overview

The **N Queens** problem is a classic algorithmic challenge where the objective is to place N queens on an N x N chessboard such that no two queens threaten each other. This means that no two queens should share the same row, column, or diagonal. This problem is a fundamental example of backtracking algorithms and is a popular exercise in understanding recursive problem-solving techniques in computer science.

## Project Description

This project implements a solution to the N Queens problem using Python and is designed to showcase your understanding of recursion and backtracking. 

### Concepts Needed

To solve this problem, you should be familiar with the following concepts:

- **Backtracking Algorithms**: Understanding how backtracking can help in systematically exploring possible placements for queens, backtracking when a conflict arises.
  - [Backtracking](https://en.wikipedia.org/wiki/Backtracking)
  
- **Recursion**: Using recursive function calls to manage the placement of queens on the board.
  - [Python Recursion](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
  
- **Data Structures**: Working with sets to track restricted columns and diagonals.
  - [Python Sets](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

- **Command Line Arguments**: Handling command-line arguments with Python’s `sys` module.
  - [Python Command Line Arguments](https://docs.python.org/3/library/sys.html#sys.argv)

By studying these concepts and utilizing the resources provided, you will be equipped to implement an efficient solution to the N Queens problem.

## Requirements

### General

- **Environment**: Files should be executable and tested on Ubuntu 20.04 LTS using Python 3.4.3 or above.
- **Coding Standards**: Code should follow PEP 8 guidelines.
- **Error Handling**: Handle incorrect input formats, such as non-integer values or values less than 4, and provide appropriate messages.
- **Execution**: Make the code executable by including the line `#!/usr/bin/python3` at the start of your file.

### Usage

To run the program, use the following command:
```bash
./nqueens.py N
```
where `N` is the size of the board and the number of queens. 

### Argument Validation

- If the incorrect number of arguments is given, display:
  ```bash
  Usage: nqueens N
  ```
- If `N` is not an integer, display:
  ```bash
  N must be a number
  ```
- If `N` is less than 4, display:
  ```bash
  N must be at least 4
  ```

## Algorithm

### Approach

This implementation uses backtracking with recursive exploration of potential placements:
1. **Track Columns and Diagonals**: Use sets to track columns, positive diagonals, and negative diagonals where queens are already placed, to ensure no two queens attack each other.
2. **Recursive Placement**: Place queens row by row and check if each column is safe.
3. **Backtrack**: If a queen placement doesn’t lead to a solution, backtrack by removing the queen and trying the next position.

### Code Structure

The solution includes:
- A command-line argument parser to validate input and call the main function.
- A main function `solve_nqueens(n)` to find all valid configurations of N queens
- A helper function `can_place_queen(row, col)` to check if a position is safe.
- A recursive function `place_nqueens(row)` to attempt queen placements and return valid configurations.

## Example

For `N = 4`, possible solutions are:
```bash
./nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

For `N = 6`, sample solutions include:
```bash
./nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
```

Each solution is a list of queen positions, where each `[row, col]` pair represents the position of a queen on the board.

## Further Reading

- [Backtracking in Algorithms](https://www.geeksforgeeks.org/backtracking-introduction/)
- [Understanding the N Queens Problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle)
