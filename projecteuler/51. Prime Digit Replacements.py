"""
presume a1|c|a2|c|...|ak|c is a prime
by keeping ai and replacing bi, we are looking for a family of *8* primes
    that conform to such a pattern.

minimum len of the number must be 2 since there's only 4 primes less than 10.
"""

from itertools import combinations
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

def get_primes(n: int, mi=2, ma=None) -> list[int]:
    fill_primes(n)
    if ma is None:
        ma = n
    return list(filter(
        lambda x: isprime(x) and mi <= x <= ma,
        range(2, n + 1)
    ))

def solve(n: int):
    dn = 2
    while True:
        mi, ma = 10 ** (dn - 1), 10 ** dn - 1
        primes = get_primes(ma, mi)

        dn_range = range(dn)
        for p in primes:
            for k in range(1, dn):
                pstr = str(p)
                for star_indices in combinations(dn_range, k):
                    pattern = ''.join(
                        ('*' if i in star_indices else pstr[i])
                        for i in dn_range
                    )
                    count = 0
                    family = list()
                    for c in range(10):
                        nv = int(pattern.replace('*', str(c)))
                        if nv > mi and isprime(nv):
                            family.append(nv)
                            count += 1

                    if count >= n:
                        return pattern, family
                    
                    continue

                    count = search(pattern, trie)
                    if count >= n:
                        return pattern, sorted(family)

                    family.clear()

        dn += 1

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(*solve(n))
