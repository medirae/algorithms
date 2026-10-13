"""
C(n, r) = n! / [ r! (n - r)! ]

-   C(n + 1, r) = (n + 1)! / [ r! (n + 1 - r)! ]
                = (n + 1) * n! / [ r! * (n + 1 - r) * (n - r)! ]
                = C(n, r) * (n + 1) / (n + 1 - r)

-   C(n, r - 1) = n! / [ (r - 1)! (n - r + 1)! ]
                = n! r / [ r! (n - r)! (n - r + 1) ]
                = C(n, r) r / (n - r + 1)
"""

from math import comb

def solve() -> int:
    mi = 10 ** 6
    n = 23
    r = 10
    c = 0

    while n <= 100:
        while r >= 0 and comb(n, r) >= mi:
            r -= 1
        
        r += 1
        c += 2 * ((n - 1) // 2 - r + 1) + int(n % 2 == 0)
        n += 1

    return c

if __name__ == '__main__':
    print(solve())
