from itertools import accumulate
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

    return is_prime, [n for n in range(2, limit + 1) if is_prime[n]]

def solve(n: int) -> int:
    is_prime, ps = primes(n)
    psn = len(ps)
    psums = [0] + list(accumulate(ps))

    best_len = best_prime = 0

    for i in range(psn):
        if i + best_len >= psn:
            break

        for j in range(i + best_len + 1, psn + 1):
            s = psums[j] - psums[i]

            if s >= n:
                break
            
            if is_prime[s]:
                best_len = j - i
                best_prime = s

    return best_prime

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(solve(n))
