"""
tldr lol
P = n(3n - 1)/2

-   P(n) ? P(n + 1)
    n(3n - 1)/2 ? (n + 1) (3n + 2) / 2
    3n^2 - n ? 3n^2 + 5n + 2
    0 ? 6n + 2
    -2 ? 6n
    -1/3 ? n
    
    1 <= n
    ?: <
    P(n) < P(n + 1)
    strictly increasing

-   j < k
    P(j) = j(3j - 1) / 2
    P(k) = k(3k - 1) / 2

    -   P(d) = P(k) - P(j)
        x = k - j -> k = x + j
        P(d) = P(x + j) - P(j)
             = (x + j)(3x + 3j - 1)/2 - j(3j - 1)/2
             = 1/2 [ (x + j)(3x + 3j - 1) - j(3j - 1) ]
             = 1/2 [ 3x^2 + 6xj - x + 3j^2 - j - 3j^2 + j ]
             = 1/2 [ 3x^2 + 6xj - x ]
             = 1/2 [ x(3x - 1) + 6xj ]
             = 3xj + x(3x - 1) / 2
             = 3xj + P(x)

        P(d) = 3(k - j)j + P(k - j)
             = 3(k - j)j + (k - j)(3(k - j) - 1)/2
             = 1/2 [ 6(k - j)j + (k - j)(3(k - j) - 1) ]
             = (k - j)/2 [ 6j + 3(k - j) - 1 ]
             = (k - j)/2 [ 6j + 3k - 3j - 1 ]
             = (k - j)/2 [ 3(k + j) - 1 ]
             = (k - j)(3(k + j) - 1)/2
        
        x = k - j, y = k + j
        P(d) = x(3y - 1)/2
        -   3d(d - 1)/2 = x(3y - 1)/2
            3d(d - 1) = x(3y - 1)
            y = (3d(d - 1)/x + 1)/3

            - x must be a divisor of 3d(d - 1)
            - y must be int

        -   1 <= k, j are int
            -   k = (y + x) / 2
                y + x must be even

            -   j = (y - x) / 2
                y - x must be positive
                x < y

    -   P(s) = P(k) + P(j)
        x = k + j -> k = x - j
        P(s) = P(x - j) + P(j)
             = (x - j)(3x - 3j - 1)/2 + j(3j - 1)/2
             = 1/2 [ 3x^2 - 3xj - x - 3xj + 3j^2 + j + 3j^2 - j ]
             = 1/2 [ 3x^2 - 6xj - x + 6j^2 ]
             = 1/2 [ 2P(x) + 6j^2 - 6xj ]
             = P(x) + 3j^2 - 3xj
             = P(x) + 3j(j - x)

        P(s) = P(k + j) - 3jk
"""

from functools import cache
from math import isqrt

@cache
def p(n: int) -> int:
    return n * (3 * n - 1) // 2

@cache
def isp(n: int) -> bool:
    if n < 0:
        return False

    root = isqrt(24 * n + 1)
    return root ** 2 == 24 * n + 1 and (1 + root) % 6 == 0

def solve():
    mi = inf = float('inf')
    k = 1
    while True:
        k += 1
        pk = p(k)
        for j in range(k - 1, 0, -1):
            pj = p(j)
            pd = pk - pj
            if mi != inf and pd >= mi:
                break

            if isp(pd) and isp(pk + pj):
                mi = pd

        if mi != inf and 3 * (k + 1) - 2 >= mi:
            return mi

if __name__ == '__main__':
    print(solve())
