#!/usr/bin/python3
"""
This module implements the isWinner function to determine the overall winner
of the Prime Game played between Maria and Ben.
"""


def isWinner(rounds, numbers):
    """
    Determines the overall winner after a given number of rounds in the
    Prime Game.

    In each round, the game is played on a set of consecutive integers
    from 1 to n, where n is provided in the 'numbers' list. In the game,
    players alternately remove a prime number and all of its multiples.
    Since the number of moves in a round equals the count of
    prime numbers up to n, Maria wins the round if this count is odd;
    otherwise, Ben wins.

    Parameters:
        rounds (int): The number of rounds to be played.
        numbers (list of int): A list of integers where each integer n
        represents a game played with numbers 1 to n.

    Returns:
        str or None: "Maria" if Maria wins more rounds,
                    "Ben" if Ben wins more rounds, or None if it is a tie
                    or if no valid rounds are provided.
    """

    """ Validate input: if there are no rounds or the number list is empty,
    no game can be played.
    """
    if not numbers or rounds <= 0:
        return None

    """Determine the maximum value in the number list to know the
    range for prime computation.
    """
    max_number = max(numbers)

    """Step 1: Use the Sieve of Eratosthenes to identify all
    prime numbers up to max_number.
    """
    is_prime = [True] * (max_number + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers.

    # Mark non-prime numbers in the sieve.
    for i in range(2, max_number + 1):
        if is_prime[i]:
            for j in range(i * i, max_number + 1, i):
                is_prime[j] = False

    """
    Step 2: Build a cumulative count array of prime numbers up to each number.
    prime_cumulative_count[i] will contain the count of primes from 1 to `i`.
    """
    prime_cumulative_count = [0] * (max_number + 1)
    for num in range(1, max_number + 1):
        prime_cumulative_count[num] = (
                prime_cumulative_count[num - 1] + (1 if is_prime[num] else 0)
        )

    """Step 3: Simulate the game for each round and count wins
    for Maria and Ben."""
    maria_wins = 0
    ben_wins = 0

    # Only consider the first 'rounds' games.
    for n in numbers[:rounds]:
        """The total number of moves available equals the number of
        primes up to n."""
        moves = prime_cumulative_count[n]
        if moves % 2 == 1:
            maria_wins += 1  # Odd number of moves: Maria wins the round.
        else:
            ben_wins += 1   # Even number of moves: Ben wins the round.

    # Step 4: Determine the overall winner.
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
