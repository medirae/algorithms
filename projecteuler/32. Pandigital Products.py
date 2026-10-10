"""
dn: digit count of multiplicand
p: power to raise 10 to
n: we want pandigital n numbers

-   multiplicand * multiplier = product
    multiplicand * 10^p = product

    take len:
    dn + (p + 1) + (dn + p)
    2dn + 2p + 1
    
-   2dn + 2p + 1 == n
    p = (n - 1) / 2 - dn

    dn = (n - 1) / 2 - p
    0 <= p <= n - 1
    1 - n <= -p <= 0
    1/2 <= (n - 1) / 2 - p <= (n - 1) / 2
    1/2 <= dn <= (n - 1) / 2
"""

from math import floor
from bisect import bisect_left

def solve(n: int) -> int:
    prods = set()
    s = 0
    target = set(map(str, range(1, n + 1)))
    for dn in range(1, floor((n - 1) / 2) + 1):
        m1_start = 10 ** (dn - 1)
        m1_end = 10 ** dn - 1
        p = floor((n - 1) / 2) - dn
        if p < 0:
            break

        m2_start = 10 ** p
        for m1 in range(m1_start, m1_end + 1):
            m1_set = set(str(m1))
            if '0' in m1_set or len(m1_set) != dn:
                continue

            m2_end = m2_start + bisect_left(
                range(m2_start, 10 ** (p + 1)), True,
                key=lambda x: dn + len(str(x)) + len(str(m1 * x)) == n
            )
            for m2 in range(m2_start, m2_end + 1):
                prod = m1 * m2
                if prod in prods:
                    continue

                prod_str = str(prod)
                prod_set = set(prod_str)
                m2_str = str(m2)
                m2_set = set(m2_str)
                union = m1_set | m2_set | prod_set
                if (
                    '0' not in m2_set and
                    '0' not in prod_set and
                    len(m2_str) == len(m2_set) and
                    len(prod_str) == len(prod_set) and
                    len(union) == n and
                    union == target and
                    not m1_set & m2_set and
                    not m1_set & prod_set and
                    not m2_set & prod_set
                ):
                    prods.add(prod)

    return sum(prods)

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(solve(n))
