from functools import reduce
from operator import or_

primes = [2, 3, 5, 7, 11, 13, 17]
ls1 = (1).__lshift__
vals = reduce(or_, map(ls1, range(10)))

def solve(n='', v=vals):
    if n.startswith('0'):
        return 0
    nn = len(n)
    if nn > 3 and int(n[-3:]) % primes[nn - 4] != 0:
        return 0

    if nn == 10:
        return int(n)

    s = 0
    ov = 0
    while v:
        b = v & -v
        v ^= b
        s += solve(n + str(b.bit_length() - 1), v | ov)
        ov |= b

    return s

if __name__ == '__main__':
    print(solve())
