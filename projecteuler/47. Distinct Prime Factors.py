def solve(k):
    limit = 1_000_000
    factors = [0] * limit

    for p in range(2, limit):
        if factors[p] == 0:  # p is prime
            for multiple in range(p, limit, p):
                factors[multiple] += 1

    streak = 0
    for n in range(2, limit):
        if factors[n] == k:
            streak += 1
            if streak == k:
                return n - (k - 1)
        else:
            streak = 0

if __name__ == '__main__':
    k = int(input('enter k: '))
    print(solve(k))
