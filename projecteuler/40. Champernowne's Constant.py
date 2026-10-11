"""
1,2,3,4,5,6,7,8,9,10,11,12,...

d(1) = 1
d(10) = 1
d(11) = 0
d(12) = 1
d(13) = 1
d(14) = 1
d(15) = 2

-   d(n)
    -   nums <= 9
        n <= 9
        d(n) = 9

    -   10 <= nums <= 99
        10 <= n <= 189

    -   100 <= nums <= 999
        190 <= n <= 2889

    -   1000 <= nums <= 9999
        2890 <= n <= 38889

    -   let r(i) be the starting range of i digit numbers
        r(1) = 1
        r(2) = 10
        r(3) = 190
        r(4) = 2890

        r(1) = 1
        r(i) = r(i - 1) + (i - 1) * 9 * 10^(i - 2)
             = [ (9i - 10) * 10^(i - 1) + 10 ] / 9

    -   let i be the rightmost value such that r(i) <= n
        let ps = 10 ** (i - 1)
        d(n) = (ps + (n - ps) // i)[(n - ps) % i]
"""

from bisect import bisect_left
from math import floor

def r(i: int) -> int:
    return ((9 * i - 10) * 10 ** (i - 1) + 10) // 9

def d(n: int) -> int:
    i = 1
    while r(i) <= n:
        i += 1
    i -= 1

    ps = 10 ** (i - 1)
    offset = n - r(i)
    num_index = offset // i
    digit_index = offset % i
    return int(str(ps + num_index)[digit_index])

def solve(n: int) -> int:
    p = 1
    for i in range(n + 1):
        p *= d(10 ** i)

    return p

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(solve(n))
