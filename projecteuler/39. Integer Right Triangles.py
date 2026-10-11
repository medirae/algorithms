"""
a, b, c
c = (a^2 + b^2)^(1/2)
1 <= a, b, c
a <= b
p = a + b + c
p <= N

-   c = sqrt(a^2 + b^2)
        sqrt(a^2 + b^2) < sqrt(a^2 + b^2 + 2ab)
        c < sqrt((a + b)^2)
        c < a + b

    -   0 < 1 <= a
        0 < a^2
        b^2 < a^2 + b^2
        b < sqrt(a^2 + b^2)
        b < c

-   p = a + b + c
    
    -   b < c < a + b
        a + 2b < p < 2a + 2b

        -   a + 2b < p <= N
            a + 2b < N
            2b < N - a
            b < (N - a) / 2

-   max a -> min b
    p <= N
    a + b + c <= N

    -   b = a ((k^2 - 1) / 2k)
        c = sqrt(a^2 + b^2)
          = sqrt(a^2 + a^2((k^2 - 1) / 2k)^2)
          = sqrt(a^2 [ 1 + ((k^2 - 1) / 2k)^2 ])
          = sqrt(a^2 [ (4k^2 + k^4 - 2k^2 + 1) / 4k^2 ])
          = sqrt(a^2 [ (k^4 + 2k^2 + 1) / 4k^2 ])
          = sqrt(a^2 [ ((k^2 + 1) / 2k)^2 ])
          = a * (k^2 + 1) / 2k

        -   a < b
            a < a (k^2 - 1) / 2k
            1 < (k^2 - 1) / 2k
            2k < k^2 - 1
            0 < k^2 - 2k - 1
            k > 1 + sqrt(2)
            k = 3

        c = 5/3 * a
        b = 4/3 * a

    -   a + b + c <= N
        a + 4/3 a + 5/3 a <= N
        3a + 4a + 5a <= 3N
        12a <= 3N
        4a <= N
        a <= N/4

-   a chosen, max b
    a + b + c <= N
    a + b + sqrt(a^2 + b^2) <= N
    a^2 + b^2 <= ((N - a) - b)^2
    a^2 + b^2 <= (N - a)^2 - 2(N - a)b + b^2
    2(N - a)b <= (N - a)^2 - a^2
    2(N - a)b <= N^2 - 2aN
    b <= (N^2 - 2aN) / 2(N - a)
"""

from collections import Counter
from math import ceil, sqrt

def solve(n: int):
    ps = Counter()
    for a in range(n // 4):
        for b in range(a + 1, ceil((n ** 2 - 2 * a * n) / (2 * (n - a))) + 1):
            c = sqrt(a ** 2 + b ** 2)
            if c != int(c):
                continue

            ps[a + b + int(c)] += 1

    ma, ma_val = 0, 0
    for p, pc in ps.items():
        if pc > ma:
            ma, ma_val = pc, p

    return ma_val

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(solve(n))
