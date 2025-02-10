#!/usr/bin/env python3

from random import randint

def openint(number: int):
    return list(map(int, str(number)[::-1]))

def closeint(numlist: list[int]):
    return sum([digit * 10**idx for idx, digit in enumerate(numlist)])

def convolution(a: list, b: list) -> list:
    m, n = len(a), len(b)
    c = [0] * ((n + m - 2) + 1)
    for k in range((n + m - 2) + 1):
        sums = 0
        for j in range(max(0, k - n), k + 1):
            if j < m and (k - j) < n:
                sums += a[j] * b[k - j]
        c[k] = sums

    return c

def test():
    for _ in range(20):
        a = randint(10**5, 10**15)
        b = randint(10**5, 10**15)
        c = convolution(openint(a), openint(b))
        assert closeint(c) == a * b, "doesn't equate..."