from functools import cache

primes_cache = {2}

def isprime(n):
    if n in primes_cache:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    for v in range(n - 1, 1, -1):
        if n % v == 0:
            return False

    primes_cache.add(n)
    return True

def is_truncatable(n):
    s = str(n)

    for i in range(1, len(s)):
        if not isprime(int(s[i:])):
            return False

    return True

def solve():
    frontier = [2, 3, 5, 7]
    found = []

    while len(found) < 11:
        next_frontier = []

        for p in frontier:
            for d in (1, 3, 7, 9):
                n = 10 * p + d

                if isprime(n):
                    next_frontier.append(n)

                    if is_truncatable(n):
                        found.append(n)

        frontier = next_frontier

    return sum(found)

if __name__ == '__main__':
    print(solve())
