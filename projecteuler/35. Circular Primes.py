from math import isqrt

def solve(n: int) -> int:
    is_prime = bytearray(b'\x01') * LIMIT
    is_prime[0:2] = b'\x00\x00'

    for p in range(2, isqrt(n - 1) + 1):
        if is_prime[p]:
            start = p ** 2
            count = (n - 1 - start) // p + 1
            is_prime[start::p] = (
                b'\x00' * count
            )

    circular_primes = set()
    visited = set()

    for n in range(2, n + 1):
        if not is_prime[n] or n in visited:
            continue

        digits = str(n)

        if len(digits) > 1 and any(
            d not in '1379' for d in digits
        ):
            continue

        rotations = {
            int(digits[r:] + digits[:r])
            for r in range(len(digits))
        }

        visited.update(rotations)

        if all(is_prime[r] for r in rotations):
            circular_primes.update(rotations)

    return len(circular_primes)

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(solve(n))
