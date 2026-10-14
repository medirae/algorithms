"""
l: square length, odd!
S(l): value at which square of size l starts
E(l): value at which square of size l ends
L(l): number of values in square of size l

-   L(l) = 4l - 4, l >= 3
    L(3) = 2

-   S(1) = E(1) = 1
    E(l) - S(l) + 1 = L(l)

    S(l) = E(l - 2) + 1
    
    -   S(l) = E(l - 2) + 1
        E(l - 2) - S(l - 2) + 1 = L(l - 2)
        E(l - 2) = L(l - 2) + S(l - 2) - 1
        S(l) = L(l - 2) + S(l - 2)

        f(x) = 4(x - 2) - 4 + f(x - 2)
             = 4x - 12 + f(x - 2)

        f(x) = 4x - 12 + f(x - 2)
        f(x - 2) = 4(x - 2) - 12 + f(x - 4)
        f(x - 4) = 4(x - 4) - 12 + f(x - 6)
        ...
        f(5) = 4*5 - 12 + f(3)
        
        -   n = (x - 3)/2 terms
        
        f(x) = f(3) + sum(i=0:n-1, 4(x - 2k) - 12)
             = 2 + sum(i=0:n-1, 4x - 8k - 12)
             = 2 + n(4x - 12) - 8n(n - 1)/2
             = 2 + n(4x - 12) - 4n(n - 1)
             = 2 + (x - 3)(4x - 12)/2 - (x - 3)(x - 5)
             = 2 + (x - 3)[ 2x - 6 - x + 5 ]
             = 2 + (x - 3)(x - 1)
             = x^2 - 4x + 5
             = (x - 2)^2 + 1

        S(l) = l^2 - 4l + 5 = (l - 2)^2 + 1
        l >= 3
    
    -   S(l) = E(l - 2) + 1
        S(l + 2) = E(l) + 1
        E(l) = S(l + 2) - 1
             = (l + 2)^2 - 4(l + 2) + 4
             = l^2 + 4l + 4 - 4l - 8 + 4
             = l^2

        E(l) = l^2
        l >= 3

-   D(l, i): value on the square of size l that sit at the corners,
        where 0 <= i < L(l)
        and   S(l) <= D(l, i) < S(l + 1)

        these will form the diangonals.
        there are always 4 of them.

    -   D(l, i) = D(l, i - 1) + l - 1
        D(l, 0) = S(l) + L(l) / 4 - 1
        D(l, i) = i(l - 1) + S(l) + L(l) / 4 - 1
                = i(l - 1) + (l - 2)^2 + 1 + l - 1 - 1
                = i(l - 1) + (l - 2)^2 + l - 1
                = il - i + l^2 - 4l + 4 + l - 1
                = il - i + l^2 - 3(l - 1)
                = l^2 - (l - 1)(3 - i)

        -   D(l, 3) = l^2, definitely not prime

        -   D(l, i) - D(l, i - 1)
            = l^2 - (l - 1)(3 - i) - l^2 + (l - 1)(4 - i)
            = (l - 1)(4 - i - 3 + i)
            = l - 1

        -   D(l, 0) = l^2 - 3(l - 1)
            = l^2 - 3l + 3    
            = l(l - 3) + 3

        -   D(l + 2, 0) - D(l, 3)
            = (l + 2)(l - 1) + 3 - l^2
            = l + 1

    -   l = 2n + 1
        D(n, i) where n is a whole number
        D(n, i) = (2n + 1)^2 - 2n(3 - i)
            = 4n^2 + 4n + 1 - 6n + 2ni
            = 4n^2 - 2n + 2ni + 1
            = 2n(2n + i - 1) + 1
            0 <= n

        -   D(n, 3)
            = 2n(2n + 2) + 1
            = 4n(n + 1) + 1

        -   D(n, 0)
            = 2n(2n - 1) + 1

        -   D(n, 0) - D(n - 1, 3)
            = 2n(2n - 1) + 1 - 4(n - 1)n - 1
            = 4n^2 - 2n - 4n^2 + 4n
            = 2n

        -   D(n, i + 1) - D(n, i)
            = 2n(2n + i) + 1 - 2n(2n + i - 1) - 1
            = 2n

        -   D(1, i) = 2i + 3
                    = 3, 5, 7, 9

            D(2, i) = 4i + 13
                    = 13, 17, 21, 25

            D(3, i) = 6i + 31
                    = 31, 37, 43, 49

-   P(n) = number of primes up until the i=3 of the nth square diagonal
    C(n) = number of diagonal numbers up until the i=3 of the nth square
    C(n) = 4n + 1

    C(n, i) where is the ith diagonal of the current nth sqaure
    C(n, i) = 1 + 4(n - 1) + i
            = 1 + i + 4(n - 1)

    goal: P(n) / C(n) < 0.1
          P(n) < 0.1 (4n + 1)
          10P(n) < 4n + 1
"""

from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False

    return True

def solve():
    prime_count = 0
    diagonal_count = 1
    side = 1

    while True:
        side += 2
        square = side * side
        step = side - 1

        for k in range(1, 4):
            if is_prime(square - k * step):
                prime_count += 1

        diagonal_count += 4

        if prime_count * 10 < diagonal_count:
            return side

if __name__ == '__main__':
    print(solve())
