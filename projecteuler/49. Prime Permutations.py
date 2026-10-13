from itertools import permutations
from math import isqrt

def primes(limit: int) -> list[int]:
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0] = is_prime[1] = 0

    for p in range(2, isqrt(limit - 1) + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : limit + 1 : p] = (
                b"\x00" * ((limit - start) // p + 1)
            )

    return [n for n in range(2, limit + 1) if is_prime[n]]

def solve(d: int) -> list[tuple[int]]:
    ps = set(filter((1000).__le__, primes(10_000)))
    v = set()

    o = list()
    for p in ps:
        pstr = str(p)
        for apstr in permutations(pstr, 4):
            if apstr == pstr:
                continue

            ap = int(''.join(apstr))
            if ap not in ps or ap in v:
                continue

            if abs(ap - p) != d:
                continue

            if ap < p and p + d in ps:
                v |= {ap, p, p + d}
                o.append((ap, p, p + d))

            if p < ap and ap + d in ps:
                v |= {p, ap, ap + d}
                o.append((p, ap, ap + d))

    return o

if __name__ == '__main__':
    d = int(input('enter d: '))
    for each in solve(d):
        print(each)
