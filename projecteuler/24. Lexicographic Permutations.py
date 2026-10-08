"""
count of permutations of n digits:
    let's say each permutation, has n positions. to fill these positions is to
     create a permutation.
    positions: _, _, ..., _, _
    the first position can take a digit in n ways. for the second position,
     since we've got 1 less digit, it can take a digit in (n - 1) ways.
     so we have: [n * (n - 1) * (n - 2) * ... * 1] = n!

assuming we're generating permutations of n digits in a lexicographic sorted way,
 and we want the kth permutation:
    for each digit position i, every (i - 1)! number of permutations later,
    digit at position i changes. the change is an ascending iteration over
    the sorted digits; but excluding the digits that are positioned in
    positions < i.
"""

from math import factorial

def solve(n: int, k: int) -> int:
    digits = list(range(n))
    o = 0
    for i in range(n, 0, -1):
        fi = factorial(i - 1)
        count = k // fi
        o += 10 ** (i - 1) * digits.pop(count)
        k -= fi * count

    return o

if __name__ == '__main__':
    n = int(input('enter n: '))
    k = int(input('enter k: ')) - 1
    print(solve(n, k))
