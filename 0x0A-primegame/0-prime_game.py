#!/usr/bin/python3
"""Prime Game"""

def isWinner(x, nums):
    """Returns name of player that won most rounds, or None if winner can't be determined.

  Args:
    x: The number of rounds.
    nums: An array of n.

  Returns:
    String representing name of winner, or None if the winner can't be determined.
    """

    if x < 1 or not nums:
        return None
    mariasWins, bensWins = 0, 0
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, isPrime in enumerate(primes, 1):
        if i == 1 or not isPrime:
            continue
        for y in range(i + i, n + 1, i):
            primes[y - 1] = False
    for _, n in zip(range(x), nums):
        primesCount = len(list(filter(lambda x: x, primes[0: n])))
        bensWins += primesCount % 2 == 0
        mariasWins += primesCount % 2 == 1
    if mariasWins == bensWins:
        return None
    return 'Maria' if mariasWins > bensWins else 'Ben'
