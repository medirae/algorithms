"""
mc: multiplicand
mcn: digit count of multiplicand
mu: multiplier
mun: digit count of multiplier
p: product
pn: digit count of product
n: pandigital digit count

-   mcn + mun - 1 <= pn <= mcn + mun

-   mc * 1, mc * 2, ..., mc * k
    n = pn_1 + pn_2 + ... + pn_k
    S = sum(i=2:k, mun_i)

    -   k <= 9
        S = k - 1

        9 < k <= 99
        S = 8 + (k - 10 + 1) * 2
          = 8 + 2k - 18
          = 2(k - 5)

        99 < k <= 999
        S = 188 + (k - 100 + 1) * 3
          = 188 + (k - 99) * 3
          = 188 + 3k - 297
          = 3k - 109

        999 < k <= 9999
        S = 2888 + (k - 1000 + 1) * 4
          = 2888 + 4k - 3996
          = 4k - 1108
          = 4(k - 277)

    -   pn_1 = mcn

        mcn + mun_2 - 1 <= pn_2 <= mcn + mun_2
        .
        .
        .
        mcn + mun_k - 1 <= pn_k <= mcn + mun_k

        =
        k * mcn + S - k + 1 <= n <= k * mcn + S
        S - k + 1 <= n - k * mcn <= S
        S - k + 1 - n <= - k * mcn <= S - n
        S - n <= k * mcn <= k - 1 - S + n
        (S - n) / k <= mcn <= (k - 1 - S + n) / k

        n=9
        (S - 9) / k <= mcn <= (k - S + 8) / k

        -   1 <= k <= 9, S = k - 1
            1 - 10/k <= mcn <= 9/k
            
            -   1 - 10/k <= mcn
                10/k <= 1 - mcn
                10/(1 - mcn) <= k
                k >= 1, mcn >= 1
                undefined
            
            -   mcn <= 9/k
                k <= 9/mcn

        -   10 <= k <= 99, S = 2k - 10
            2 - 19/k <= mcn <= 18/k - 1
            
            -   2 - 19/k <= mcn
                2 - mcn <= 19/k
                k >= 19/(2 - mcn)
                for every mcn=1 -> k >= 19
                otherwise undefined
            
            -   mcn <= 18/k - 1
                k <= 18 / (mcn + 1)

        -   100 <= k <= 999, S = 3k - 109
            3 - 118/k <= mcn <= 117/k - 2

            -   3 - 118/k <= mcn
                118/(3 - mcn) >= k
                for every mcn=1 -> k <= 59
                for every mcn=2 -> k <= 118
                otherwise undefined

            -   mcn <= 117/k - 2
                k <= 117 / (mcn + 2)

        -   1000 <= k <= 9999, S = 4k - 1108
            4 - 1117/k <= mcn <= 1116/k - 3

            -   4 - 1117/k <= mcn
                1117 / (4 - mcn) >= k
                for every mcn=1 -> k <= 372
                for every mcn=2 -> k <= 558
                for every mcn=3 -> k <= 1117
                otherwise undefined

            -   mcn <= 1116/k - 3
                k <= 1116 / (mcn + 3)
"""

from math import floor
from bisect import bisect_left
from collections import Counter

def solve(n: int) -> int:
    target = Counter(map(str, range(1, n + 1)))
    empty = Counter({k: 0 for k in range(1, 10)})
    maxi = 0
    for mcn in range(5, 0, -1):
        k4r = floor(1116 / (mcn + 3))

        mcnl = 10 ** (mcn - 1)
        mcnr = 10 ** mcn - 1
        for mc in range(mcnr, mcnl - 1, -1):
            p_set = empty.copy()
            num = ''
            for k in range(1, k4r + 1):
                p = str(mc * k)
                num += p
                p_set += Counter(p)
                if not (p_set <= target):
                    break

                if p_set == target and int(num) > maxi:
                    maxi = int(num)

    return maxi

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(solve(n))

