"""
s <= x1 <= e
s <= x2 <= e
x1 ^ x2

-------------
b1^x1 = b2^x2
s <= b1, x1 <= e
s <= b2 < b1

-   b2 < b1
    b2^x2 < b1^x2
    b1^x1 < b1^x2
    x1 < x2

    s <= b2
    s^x2 <= b2^x2
    s^x2 <= b1^x1
    x2 log[b1](s) <= x1
    x2 <= x1 / log[b1](s)

-   b1^x1 = b2^x2
    x1 = x2 log[b1](b2)

    -   s <= x1 <= e
        s / log[b1](b2) <= x2 <= e / log[b1](b2)

    -   since b2 < b1 -> 0 < log[b1](b2) < 1

    -   x1 must be int
        x2 * log[b1](b2) must be int
    
-   b1 = p1^k1 * p2^k2 ... * pn^kn = mul(p1i ^ k1i) = P1
    b2 = mul(p2i ^ k2i) = P2

    -   x1 = x2 * log[b1](b2)
        x1 = x2 * log[P1](P2)

        -   0 < b2 < b1
            0 < log[P1](P2) < 1
            log[P1](P2) = c/d where c and d are int

        -   x1 must be int
            x2 * log[P1](P2) must be int
            x2 * c/d must be int
            x2 must be a multiple of d

    -   assume: the set of primes in p1i are exactly as the set of
            primes in p2i.

        P1 / P2 = mul(pi ^ (k1i - k2i))
        k1i and k2i are int
        k1i >= k2i


basically numbers are duplicated when with a given set of primes, powers greater than 1 make redundant numbers.
"""

from itertools import combinations, chain
from collections import Counter
from functools import reduce
from operator import mul

prime_cache = {2}

def isprime(n: int) -> bool:
    if n <= 1 or n % 2 == 0:
        return False

    if n in prime_cache:
        return True

    for i in prime_cache:
        if n % i == 0:
            return False

    prime_cache.add(n)
    return True

def mk_prime_sets(mi: int, ma: int) -> list[tuple[int]]:
    primes = [x for x in range(mi, ma + 1) if isprime(x)]
    o = list()
    for r in range(1, len(primes) + 1):
        for s in combinations(primes, r):
            if reduce(mul, s, 1) >= ma:
                break

            o.append(s)

    return o

pr_min = 

def calc_powers(pset: Counter, mi: int, ma: int) -> int:
    bm = reduce(mul, (pr ** po for pr, po in pset.items()), 1)
    if not (mi <= bm <= ma):
        return 0

    c = 1
    for pr in pset:
        if bm * pr <= ma:
            pset[pr] += 1
            c += calc_powers(pset, mi, ma)
            pset[pr] -= 1

    return c

def mk_reduntants(mi: int, ma: int):
    c = 0
    prime_sets = mk_prime_sets(mi, ma)
    for prime_set in prime_sets:
        pset = Counter({p: 1 for p in prime_set})
        for pos in range(len(prime_set)):
            pset[prime_set[pos]] += 1
            c += calc_powers(pset, mi, ma)
            pset[prime_set[pos]] -= 1

    return c

print(mk_reduntants(2, 100))

## TODO: left unfinished.
# I have write a way to filter correctly! I'm filtering the values produced via primes, that's wrong.
# I should instead take b1 over (mi, ma) and then take b2 as the divisors of b1 and then calculate the contraints of b2^x2, and then take the prime factors of b2 and extend the maximum for that power set!
# just too complicated...
