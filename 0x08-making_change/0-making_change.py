#!/usr/bin/python3
"""
Module for determining the minimum number of coins needed to meet a
given amount total. The function uses a recursive dynamic programming
approach with memoization to find the optimal solution.
"""


def makeChange(coins: list[int], total: int) -> int:
    """
    Function to determine the minimum number of coins required to meet a
    total using a recursive dynamic programming approach.

    This function calculates the minimum number of coins needed to
    reach the target total using an infinite supply of coins from
    the given denominations. The solution uses memoization to optimize
    recursive calls and avoid redundant calculations.

    Args:
        coins (list): List of coin denominations (positive integers).
        total (int): Target amount to achieve.

    Returns:
        int: Minimum number of coins required to meet the total.
             Returns 0 if the total is 0 or less.
             Returns -1 if the total cannot be met with the given coins.
    """

    def dp_recursive(coins, total, memo):
        if total == 0:
            return 0
        if total < 0:
            return float('inf')
        if total in memo:
            return memo[total]

        min_coins = float('inf')

        for coin in coins:
            res = dp_recursive(coins, total - coin, memo)
            if res != float('inf'):
                min_coins = min(min_coins, res + 1)

        memo[total] = min_coins
        return min_coins

    if total <= 0:
        return 0

    result = dp_recursive(coins, total, {})
    return result if result != float('inf') else -1
