#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    write a method that calculates the fewest number of operations
    """
    dp = [0] * (n + 1)

    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = float('inf')

        for j in range(1, i):
            dp[i] = min(dp[i], dp[j] + dp[i - j])

    if dp[n] == float('inf'):
        return 0
    else:
        return dp[n]
