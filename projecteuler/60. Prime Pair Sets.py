from collections import namedtuple
from functools import partial
from math import isqrt
from time import perf_counter_ns

def psieve(n: int) -> bytearray:
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'

    for p in range(2, isqrt(n) + 1):
        if not sieve[p]:
            continue

        start = p * p
        count = (n - start) // p + 1
        sieve[start::p] = b"\x00" * count

    return sieve

def search_limit(LIMIT: int) -> int:
    result = namedtuple('result', ['mi', 'set'])
    r = result(float('inf'), ())

    sieve = psieve(LIMIT ** 2)
    primes = [x for x in range(3, LIMIT + 1, 2) if sieve[x]]
    isprime = lambda n: bool(sieve[n])

    shifts, dsum, compatibles = dict(), dict(), dict()
    for p in primes:
        pstr = str(p)
        shifts[p] = 10 ** len(pstr)
        dsum[p] = sum(map(int, pstr))
        compatibles[p] = set()

    for i, p in enumerate(primes):
        for ap in primes[i + 1:]:
            if (dsum[p] + dsum[ap]) % 3 == 0:
                continue

            if not isprime(p * shifts[ap] + ap):
                continue

            if not isprime(p + ap * shifts[p]):
                continue

            compatibles[p].add(ap)

    def bt(picked: list[int], candidates: list[int], s: int):
        nonlocal r
        need = n - len(picked)
        if need == 0:
            r = result(s, tuple(picked))
            return

        if len(candidates) < need:
            return

        if s + sum(candidates[:need]) >= r.mi:
            return

        for i, p in enumerate(candidates):
            if s + p >= r.mi:
                break

            aprimes = candidates[i + 1:]
            if len(aprimes) < need - 1:
                break

            next_candidates = [ap for ap in aprimes if ap in compatibles[p]]
            if len(next_candidates) < need - 1:
                continue

            if s + p + sum(next_candidates[:need - 1]) >= r.mi:
                continue

            bt(picked + [p], next_candidates, s + p)

    bt([], primes, 0)
    return r.mi, r.set

def solve(n: int) -> tuple[int, tuple]:
    i = 1
    LIMIT = 500
    mi, mi_set = float('inf'), ()
    while True:
        print(f'- looking in primes range ..{LIMIT}')
        try:
            mi, mi_set = search_limit(LIMIT)
            if mi != float('inf'):
                break
        except IndexError:
            pass

        LIMIT = LIMIT * ((7 + 3 * (-1) ** i) // 2)
        i = not i

    return mi, mi_set

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(solve(n))
