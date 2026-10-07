from collections import Counter
from itertools import product
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

def is_amicable(n: int) -> bool:
    return get_divisor_sum(n) != n and get_divisor_sum(get_divisor_sum(n)) == n

def sum_amicables(n: int) -> bool:
    s = 0
    for i in range(1, n):
        if is_amicable(i):
            s += i
    
    return s

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(sum_amicables(n))
