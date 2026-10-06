from math import sqrt, ceil
from functools import reduce
from operator import mul, or_
from collections import Counter
from itertools import starmap

primes = {1: Counter(), 2: Counter({2: 1})}

def eval_primes(n: int) -> Counter:
    if n in primes:
        return primes[n]
    
    for v in range(ceil(sqrt(n)), 1, -1):
        if n % v == 0:
            return primes.setdefault(n, eval_primes(v) + eval_primes(n // v))

    primes[n] = Counter({n: 1})
    return primes[n]

p1 = (1).__add__

def divisor_count(n: int) -> int:
    return reduce(mul, map(p1, eval_primes(n).values()), 1)

def triangle_num_with_n_primes(n: int) -> int:
    s = 3
    i = 2
    while divisor_count(s) < n:
        i += 1
        s += i
    
    return s

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(triangle_num_with_n_primes(n))

