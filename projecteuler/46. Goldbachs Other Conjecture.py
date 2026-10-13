"""
n = p + 2 * a^2

-   a + b = c
    
    -   odd + odd
        2i + 1 + 2j + 1
        = 2(i + j + 1)
        even

    -   odd + even
        2i + 1 + 2j
        = 2(i + j) + 1
        odd

    -   even + even
        2i + 2j
        = 2(i + j)
        even

-   n - p = 2 * a^2
    (n - p) / 2 = a^2
    sqrt((n - p) / 2) = a

    -   n - p must be even and positive
        -   p = 2
            n must be even
            n > 2

        -   p is odd
            n must be odd
            n > p

    -   sqrt((n - p) / 2) must be perfect squre
"""

from math import sqrt, isqrt

is_prime = bytearray([0, 0])

def isprime(n: int) -> bool:
    return bool(is_prime[n])

def fill_primes(n: int) -> None:
    last = len(is_prime) - 1

    if (d := n - last) > 0:
        is_prime.extend(b'\x01' * d)
    else:
        return

    for p in range(2, isqrt(n) + 1):
        if not is_prime[p]:
            continue

        first = ((last + 1 + p - 1) // p) * p
        start = max(p * p, first)
        if start <= n:
            count = (n - start) // p + 1
            is_prime[start : n + 1 : p] = b"\x00" * count

def primes(n: int) -> list[int]:
    return [n for n in range(2, n + 1) if is_prime[n]]

def solve():
    n = 9
    while True:
        fill_primes(n)
        for p in primes(n):
            a = sqrt((n - p) / 2)
            if int(a) == a:
                break
        else:
            return n

        n += 2

if __name__ == '__main__':
    print(solve())
