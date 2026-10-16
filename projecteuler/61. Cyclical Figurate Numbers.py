"""
T(t) = t(t + 1)/2
-   1000 <= T(t) <= 9999
    1000 <= t(t + 1)/2 <= 9999
    2000 <= t^2 + t <= 19998
    -   t^2 + t - 2000 >= 0
        t >= 45

    -   t^2 + t - 19998 <= 0
        t <= 140

    45 <= t <= 140

S(s) = s^2
-   1000 <= S(s) <= 9999
    1000 <= s^2 <= 9999
    32 <= s <= 99

P(p) = p(3p - 1)/2
-   1000 <= P(p) <= 9999
    1000 <= p(3p - 1)/2 <= 9999
    2000 <= 3p^2 - p <= 19998
    -   3p^2 - p - 2000 >= 0
        p >= 26

    -   3p^2 - p - 19998 <= 0
        p <= 81

    26 <= p <= 81

Hx(x) = x(2x - 1)
-   1000 <= Hx(x) <= 9999
    1000 <= x(2x - 1) <= 9999
    23 <= x <= 70

Hp(h) = h(5h - 3)/2
-   1000 <= h(5h - 3)/2 <= 9999
    21 <= h <= 63

O(o) = o(3o - 2)
-   19 <= o <= 58
"""

from collections import defaultdict

polygonals = {
    't': [t * (t + 1) // 2 for t in range(45, 141)],
    's': [s ** 2 for s in range(32, 100)],
    'p': [p * (3 * p - 1) // 2 for p in range(26, 82)],
    'hx': [x * (2 * x - 1) for x in range(23, 71)],
    'hp': [h * (5 * h - 3) // 2 for h in range(21, 64)],
    'o': [o * (3 * o - 2) for o in range(19, 59)],
}

g = defaultdict(list)
for kind, numbers in polygonals.items():
    for n in numbers:
        if n % 100 >= 10:
            g[n // 100].append((n, kind))

vals = list()
kinds = list()
def bt(val: int):
    ds = val % 100
    if len(vals) == 6:
        if vals[0] // 100 == ds:
            return list(zip(kinds, vals))

        return

    for av, kind in g[ds]:
        if kind not in kinds:
            vals.append(av)
            kinds.append(kind)
            if (v := bt(av)) is not None:
                return v
            kinds.pop()
            vals.pop()

for val in polygonals['o']:
    vals.append(val)
    kinds.append('o')
    if (v := bt(val)) is not None:
        print(v)
        print(sum(i[1] for i in v))
        break
    kinds.pop()
    vals.pop()
