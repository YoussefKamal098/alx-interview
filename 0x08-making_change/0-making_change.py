#!/usr/bin/python3
"""
Module for determining the minimum number of coins needed to meet a
given amount total. The function uses an iterative dynamic programming
approach to find the optimal solution.
"""


def makeChange(coins, total):
    """
    Function to determine the minimum number of coins required to meet a
    total using an iterative dynamic programming approach.

    This function calculates the minimum number of coins needed to
    reach the target total using an infinite supply of coins from
    the given denominations. The solution uses an iterative approach
    to fill a dynamic programming table and find the optimal solution.

    Args:
        coins (list): List of coin denominations (positive integers).
        total (int): Target amount to achieve.

    Returns:
        int: Minimum number of coins required to meet the total.
             Returns 0 if the total is 0 or less.
             Returns -1 if the total cannot be met with the given coins.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
