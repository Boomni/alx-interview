#!/usr/bin/python3
""" Make change module"""


def makeChange(coins, total):
    '''Makes change'''

    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    count = 0
    coins.sort()
    coins.reverse()
    for coin in coins:
        while coin <= total:
            total -= coin
            count += 1
        if (total == 0):
            return count
    return -1
