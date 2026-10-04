from math import sqrt, ceil
from functools import reduce
from operator import mul, or_
from collections import Counter
from itertools import starmap

primes = {1: Counter(), 2: Counter({2: 1})}

def eval_primes(n: int) -> set:
    if n in primes:
        return primes[n]
    
    for v in range(ceil(sqrt(n)), 1, -1):
        if n % v == 0:
            return primes.setdefault(n, eval_primes(v) + eval_primes(n // v))

    primes[n] = Counter({n: 1})
    return primes[n]

def smallest_multiple(n: int):
    primes = reduce(or_, (eval_primes(v) for v in range(2, n + 1)), Counter())
    return reduce(mul, starmap(pow, primes.items()), 1)

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(smallest_multiple(n))
