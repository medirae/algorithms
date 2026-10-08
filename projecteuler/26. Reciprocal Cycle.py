def fractions(n: int) -> list[int]:
    o = list()
    rs = set()
    q, r = int(1 // n), 1 % n
    while r not in rs:
        rs.add(r)
        r *= 10
        q, r = int(r // n), r % n
        o.append(q)

    return o if 0 not in rs else list()

def solve(n: int):
    ma, val = 0, 1
    for i in range(1, n):
        if (l := len(fractions(i))) > ma:
            ma = l
            val = i

    return val

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(solve(n))
