from collections import Counter
from itertools import product, takewhile, chain
from functools import reduce
from operator import mul

factors_cache = {2: Counter({2: 1})}
primes_cache = {2}

def get_factors(n: int) -> dict:
    if n in factors_cache:
        return factors_cache[n]

    if n in primes_cache:
        return Counter({n: 1})

    for v in range(n - 1, 1, -1):
        if n % v == 0:
            factors_cache[n] = get_factors(v) + get_factors(n // v)
            return factors_cache[n]

    primes_cache.add(n)
    return Counter({n: 1})

divisors = dict()

def get_divisors(n: int) -> set:
    if n in divisors:
        return divisors[n]

    if n in primes_cache or n == 1:
        return {1}

    factors = get_factors(n)
    o = set()
    for p, c in factors.items():
        an = int((p ** (c - 1)) * n / (p ** c))
        o |= {an} | get_divisors(an)

    divisors[n] = o
    return divisors[n]

divisor_sums = dict()

def get_divisor_sum(n: int) -> int:
    if n in divisor_sums:
        return divisor_sums[n]
    
    divisor_sums[n] = sum(get_divisors(n))
    return divisor_sums[n]

def is_abundant(n: int) -> str:
    return n < get_divisor_sum(n)

def get_sums_of__not_abundant_summeds(n: int) -> int:
    abundants = [i for i in range(1, n + 1) if is_abundant(i)]
    abundant_sums = sum(set(chain.from_iterable(
        takewhile(n.__ge__, (a + b for b in abundants))
        for a in abundants
    )))
    return n * (n + 1) // 2 - abundant_sums

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(get_sums_of__not_abundant_summeds(n))
