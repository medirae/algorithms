from functools import cache

coins = [1, 2, 5, 10, 20, 50, 100, 200]
N = len(coins)

@cache
def solve(r: int, ndx: int = 0) -> int:
    if r == 0:
        return 1

    if ndx == N:
        return 0

    s = 0
    if coins[ndx] <= r:
        s += solve(r - coins[ndx], ndx)

    for i in range(ndx + 1, N):
        if coins[i] > r:
            break

        s += solve(r - coins[i], i)

    return s

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(solve(n))
