from bisect import bisect_left
from math import hypot
from collections import defaultdict

def valid_pyth_triplet_before_n(n: int) -> int:
    sqrd = defaultdict(list)
    for a in range(1, n // 2 + 1):
        for b in range(a + 1, n // 2 + 1):
            sqrd[a ** 2 + b ** 2].append((a, b))

    for c in range(1, n // 2 + 1):
        for a, b in sqrd[c ** 2]:
            if a + b + c == n:
                return a * b * c

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(valid_pyth_triplet_before_n(n))
