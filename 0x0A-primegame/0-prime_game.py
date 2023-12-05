#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """
    Determines the winner of a game

    Args:
        x: Number of rounds played.
        nums: List of integers for each round.

    Returns:
        None if the winner cannot be determined, "Maria" if Maria wins,
        "Ben" if Ben wins.
    """

    maria_wins, ben_wins = 0, 0

    for i in range(x):
        n = nums[i]
        primes = [j for j in range(2, n + 1) if is_prime(j)]

        maria_turn = True
        while primes:
            if maria_turn:
                # Maria picks a prime
                prime = primes.pop(0)
                for j in range(prime, n + 1, prime):
                    if j in primes:
                        primes.remove(j)
                maria_turn = False
            else:
                # Ben picks a prime
                prime = primes.pop(0)
                for j in range(prime, n + 1, prime):
                    if j in primes:
                        primes.remove(j)
                maria_turn = True

        if maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.
    """

    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
