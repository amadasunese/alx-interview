#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    max_value = float('inf')
    dp = [max_value] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                sub_result = dp[i - coin]
                if sub_result != max_value and sub_result + 1 < dp[i]:
                    dp[i] = sub_result + 1

    return -1 if dp[total] == max_value else dp[total]
