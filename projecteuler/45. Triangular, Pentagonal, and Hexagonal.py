"""
T(n) = n(n + 1)/2
P(n) = n(3n - 1)/2
H(n) = n(2n - 1)

T(i) = P(j) = H(k)

-   T(i) = H(k)
    i(i + 1)/2 = k(2k - 1)

    i^2 + i = 2k^2 - k

    -   k(2k - 1) = (2k - 1)(2k)/2 = T(2k - 1)
        T(i) = H(k) = T(2k - 1)
        i = 2k - 1
        k = (i + 1)/2
        i must be odd

-   T(i) = P(j)
    i(i + 1)/2 = j(3j - 1)/2
    i = 2k - 1
    2k(2k - 1)/2 = j(3j - 1)/2
    4k^2 - 2k = 3j^2 - j
    (2k - 1/2)^2 = 3j^2 - j + 1/4
    (4k - 1)^2 = 12j^2 - 4j + 1
    3(4k - 1)^2 = (6j - 1)^2 + 2

    (6j - 1)^2 - 3(4k - 1)^2 = -2
    -   Pell equation: x^2 - Dy^2 = N
        x = 6j - 1, x = -1 mod 6 = 5 mod 6
        y = 4k - 1, y = -1 mod 4 = 3 mod 4
        D = 3
        N = -2

    (6j - 1)^2 = 3(4k - 1)^2 - 2
    6j - 1 = sqrt[ 3(4k - 1)^2 - 2 ]
    j = ( sqrt[ 3(4k - 1)^2 - 2 ] + 1 ) / 6
    
"""

from math import sqrt

def solve(n: int) -> int:
    i = n + 1 + int(n & 1)
    while True:
        k = (i + 1) // 2
        y = 4 * k - 1
        if y % 4 != 3:
            i += 2
            continue

        x = sqrt( 3 * ((4 * k - 1) ** 2) - 2 )
        if x % 6 != 5 or int(x) != x:
            i += 2
            continue

        return i

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(solve(n))
