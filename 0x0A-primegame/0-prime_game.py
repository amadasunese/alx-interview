#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_next_prime(numbers):
        for num in numbers:
            if is_prime(num):
                return num
        return None

    def play_game(round_numbers):
        current_player = "Maria"
        while True:
            prime = get_next_prime(round_numbers)
            if prime is None:
                return current_player
            round_numbers = [num for num in round_numbers if num % prime != 0]
            current_player = "Ben" if current_player == "Maria" else "Maria"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(list(range(1, n + 1)))
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
x = 3
nums = [4, 5, 1]
result = isWinner(x, nums)
print(result)

