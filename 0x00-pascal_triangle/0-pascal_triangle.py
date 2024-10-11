#!/usr/bin/python3

"""
Pascal's Triangle Generator

This script defines a function `pascal_triangle(n)` that generates the
first n rows of Pascal's Triangle. Pascal's Triangle is a triangular
array where each entry is the sum of the two entries directly above it.
The function handles edge cases for invalid inputs (n <= 0) and
returns an appropriate structure for valid inputs.

Usage:
    result = pascal_triangle(n)  # where n is the number of rows to generate

Returns:
    A list of lists representing the first n rows of Pascal's Triangle.
    If n is less than or equal to 0, an empty list is returned.
"""


def pascal_triangle(n):
    """
    Generate the first n rows of Pascal's Triangle.

    Pascal's Triangle is a triangular array of the
    binomial coefficients. Each number is the sum of the
    two numbers directly above it.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        List[List[int]]: A list of lists representing the first n rows of
                         Pascal's Triangle. If n is less than or equal to 0,
                         returns an empty list.
    """
    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        return []

    # If n is 1, return the first row of the triangle
    if n == 1:
        return [[1]]

    # If n is 2, return the first two rows of the triangle
    if n == 2:
        return [[1], [1, 1]]

    # Initialize the triangle with the first two rows
    triangle = [[1], [1, 1]]

    # Loop to generate rows from the third row to the nth row
    for i in range(2, n):
        # Create a new row initialized with 1's
        row = [1] * (i + 1)

        # Fill in the inner values of the row
        for j in range(1, i):
            # Each value is the sum of the two values above it in the triangle
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Append the newly created row to the triangle
        triangle.append(row)

    # Return the complete triangle
    return triangle
