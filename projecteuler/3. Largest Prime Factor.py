from math import sqrt, ceil

primes = {1: set(), 2: {2}}

def eval_primes(n: int) -> set:
    if n in primes:
        return primes[n]
    
    for v in range(ceil(sqrt(n)), 1, -1):
        if n % v == 0:
            return primes.setdefault(n, eval_primes(v) | eval_primes(n // v))

    primes[n] = {n}
    return primes[n]

def largest_prime(n: int) -> int:
    return max(eval_primes(n))

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(largest_prime(n))
