"""
for grid size = n, we have n decisions per side.
representing decisions as _, _, ..., _, _:
    each path from top-left to down-right consists of 2n decisions of either r or d.
    in each sequence, if the selected decision isn't r, it's d!
    therefore having R = sum(r) = n, D = sum(d) = n, we have R == D and R + D == 2n.
    therefore if we pick R=n decisions from all the 2n decisions, the rest can be automatically derived.
    therefore sequence counts = comb(2n, n)
"""

from math import comb

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(comb(2 * n, n))
