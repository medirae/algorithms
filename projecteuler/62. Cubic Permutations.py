"""
-   dn = digit count of number
    10^(dn - 1) <= n^3 <= 10^n - 1
    ceil((10^(dn - 1))^(1/3)) <= n <= floor((10^n - 1)^(1/3))
"""

from math import floor, ceil
from bisect import insort

dn = 1
N = 5
while True:
    mi = ceil((10 ** (dn - 1)) ** (1/3))
    ma = floor((10 ** dn - 1) ** (1/3))
    print(f'{dn=}')
    print(f'attempting:\n\t{mi} <= v <= {ma}\n\t{mi**3} <= c <= {ma**3}\n')

    trie = dict()
    for v in range(mi, ma + 1):
        c = v ** 3
        cstr = sorted(str(c))
        d = trie
        for digit in cstr:
            if digit not in d:
                d[digit] = dict()

            d = d[digit]

        if 'vals' not in d:
            d['vals'] = list()

        insort(d['vals'], c)

    def dfs(d):
        if 'vals' in d and len(d['vals']) == N:
            return d['vals']

        mi = float('inf')
        mi_set = list()
        for digit in d:
            if digit.isnumeric():
                v = dfs(d[digit])
                if v and v[0] < mi:
                    mi = v[0]
                    mi_set = v

        return mi_set
    
    mi_set = dfs(trie)
    if mi_set:
        print(mi_set)
        break

    dn += 1
