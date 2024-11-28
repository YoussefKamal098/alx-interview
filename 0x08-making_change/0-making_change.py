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
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
