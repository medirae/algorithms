"""
```typst
#set page(fill: rgb("0d1117"))
#set text(fill: rgb("f0f6fc"))
#set align(left)
#show math.equation.where(block: true): set align(left)

== Expansion of #math.sqrt([23])
$
#let srt = [#math.sqrt([23])]

a_0 = 4&, 1/(srt - 4) (srt + 4) / (srt + 4) = (srt + 4) / (23 - 16) = (srt + 4) / 7 = 1 + (srt - 3) / 7 \
a_1 = 1&, 7 / (srt - 3) (srt + 3) / (srt + 3) = 7 (srt + 3) / (23 - 9) = 7/14 (srt + 3) = (srt + 3) / 2 = 3 + (srt - 3) / 2 \
a_2 = 3&, 2 / (srt - 3) (srt + 3) / (srt + 3) = 2/14 (srt + 3) = (srt + 3) / 7 = 1 + (srt - 4) / 7 \
a_3 = 4&, 7 / (srt - 4) (srt + 4) / (srt + 4) = srt + 4 = 8 + srt - 4 \
a_4 = 8&, 1/(srt - 4) (srt + 4) / (srt - 4) = (srt + 4) / 7 = 1 + (srt - 4) / 7 \
$

#linebreak()

== Numenator vs Denominator Alignment
$
#let srt = [#math.sqrt([23])]
#let nu = [nu]
#let de = [de]

0 <= (srt + nu) / de <= 1 \
0 <= srt + nu <= de \
-srt <= nu <= de - srt
$
```
"""

from math import isqrt, sqrt, gcd

def next_fraction(root, a, nu, de):
    sr = sqrt(root)
    nde = root - nu ** 2
    nu_m = de
    g = gcd(nde, nu_m)
    nde //= g
    nu_m //= g
    
    nnu = abs(nu)
    na = 0
    nde_m = nde // nu_m
    while not (-sr <= nnu <= nde_m - sr):
        nnu -= nde_m
        na += 1

    return root, na, nnu * nu_m, nde

def find_fractions(root: int):
    ps = isqrt(root)
    if ps == sqrt(root):
        return ()
    v = set()
    fracs = list()

    frac = (root, ps, -ps, 1)
    while frac not in v:
        v.add(frac)
        fracs.append(frac[1])
        frac = next_fraction(*frac)

    return fracs

c = 0
for i in range(2, 10_001):
    fracs = find_fractions(i)
    ln = len(fracs) - 1
    if ln < 0:
        continue
    c += int(ln & 1)

print(c)
