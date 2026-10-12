from collections import Counter
from math import isqrt

def primes(limit: int) -> list[int]:
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0] = is_prime[1] = 0

    for p in range(2, isqrt(limit - 1) + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : limit + 1 : p] = (
                b"\x00" * ((limit - start) // p + 1)
            )

    return [n for n in range(2, limit + 1) if is_prime[n]]

def is_pandigital(n: int) -> bool:
    mask = 0
    count = 0

    while n:
        digit = n % 10
        bit = 1 << digit

        if digit == 0 or mask & bit:
            return False

        mask |= bit
        count += 1
        n //= 10

    return mask == (1 << (count + 1)) - 2

def solve():
    ma = 0
    for p in primes(10_000_000):
        if is_pandigital(p) and p > ma:
            ma = p

    return p

if __name__ == '__main__':
    print(solve())
