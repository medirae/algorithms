"""
dn = digit count of a number
dn > 0

-   10^(dn - 1) <= n <= 10^dn - 1
    x is a natural number
    10^(dn - 1) <= x^dn <= 10^dn - 1

    -   it can be observed that 10^dn will always produce a (dn + 1) number
        therefore x <= 9

    -   10^(dn - 1) <= 9^dn
        (dn - 1) log[10](10) <= dn log[10](9)
        dn (1 - log[10](9)) <= 1
        dn <= 1 / (1 - log[10](9))
        dn <= 21.85
        dn <= 21

    -   10^(dn - 1) <= x^dn
        10^((dn - 1)/dn) <= x
        ceil(10^((dn - 1)/dn)) <= x
"""

from math import ceil

c = 0
for dn in range(1, 22):
    mi = 10 ** (dn - 1)
    ma = 10 ** dn - 1

    xmi = ceil(10 ** ((dn - 1) / dn))
    for x in range(xmi, 10):
        c += mi <= x ** dn <= ma
        print(f'{mi} <= {x}^{dn} = {x ** dn} <= {ma}')

print()
print(c)
