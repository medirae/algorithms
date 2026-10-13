def solve(n, k) -> int:
    mod = 10 ** k
    s = 0
    for i in range(1, n + 1):
        s += pow(i, i, mod)

    return s % mod

if __name__ == '__main__':
    n = int(input('enter n: '))
    k = int(input('enter k: '))
    print(solve(n, k))
