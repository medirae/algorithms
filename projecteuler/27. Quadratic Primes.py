"""
fn = n^2 + an + b, 0 <= n < x, must be a prime producing equation.

n = 0:
    fn = b must be prime!
n = 1:
    fn = (1 + a + b) must be prime!
       if b = 2 -> (3 + a) must be prime
            (3 + a) must be odd
            -> a must be even
            (3 + a) > 0
            -> a > -3
       elif (b + 1 + a) must be odd and positive
            (b + 1 + a) is odd
         -> a must be odd
            (b + 1 + a) > 2
         -> a > 1 - b
"""

primes = {2}

def isprime(n: int) -> bool:
    if n <= 1 or n % 2 == 0:
        return False

    if n in primes:
        return True

    for i in primes:
        if n % i == 0:
            return False

    primes.add(n)
    return True

def count_primes(a: int, b: int) -> int:
    fn = lambda n: n**2 + a * n + b
    n = 0
    while isprime(fn(n)):
        n += 1

    return n

def solve(n: int) -> int:
    ma_count, ma_coeff = 0, 0
    for a in range(-2, n + 1, 2):
        if not isprime(a + 3):
            continue

        if (c := count_primes(a, 2)) > ma_count:
            ma_count, ma_coeff = c, a * 2

    for b in range(n - int(n % 2 == 0), 2, -2):
        if not isprime(b):
            continue

        for a in range(n - int(n % 2 == 0), 1 - b, -2):
            if not isprime(a + b + 1):
                continue

            if (c := count_primes(a, b)) > ma_count:
                ma_count, ma_coeff = c, a * b

    return ma_coeff

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(solve(n))
