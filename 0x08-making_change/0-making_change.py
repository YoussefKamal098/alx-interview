#!/usr/bin/python3
"""
Determines the minimum number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Function to determine the minimum number of coins required
    to meet a total.

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

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total <= 0:
            break
        num_coins = total // coin
        count += num_coins
        total -= num_coins * coin

    return count if total == 0 else -1
