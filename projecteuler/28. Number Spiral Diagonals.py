def solve(n):
    s = 1
    for i in range(3, n + 1, 2):
        i2 = i ** 2
        s += sum(range((i - 2) ** 2 + i - 1, i ** 2 + 1, i - 1))

    return s

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(solve(n))
