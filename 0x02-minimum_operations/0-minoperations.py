#!/usr/bin/python3
"""
Module to calculate the minimum number of operations required to
achieve exactly n 'H' characters in a file starting with one 'H'.
The operations allowed are Copy All and Paste.

Functions:
    minOperations(n): Returns the minimum number of operations
    required to reach n 'H' characters in the file, or 0 if n
    is less than 2.
"""


def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations needed to get exactly n 'H'
    characters in a file, starting with one 'H'. The allowed operations are:
    - Copy All: Copy all current characters in the file.
    - Paste: Paste the copied characters.

    This function uses a greedy approach, factoring n to determine the optimal
    sequence of operations. For every factor found, it simulates the Copy All
    followed by multiple Paste operations to reach the next factor.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations needed, or 0 if n is less
        than 2.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
