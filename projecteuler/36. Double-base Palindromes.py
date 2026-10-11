from functools import cache

@cache
def gen(n: int):
    if n == 1:
        return tuple(str(i) for i in range(10))

    if n == 2:
        return tuple(2 * str(i) for i in range(10))

    return tuple(f'{i}{mid}{i}' for i in range(10) for mid in gen(n - 2))

def solve(n: int) -> int:
    s = 0
    for d in range(1, len(str(n - 1)) + 1):
        for pal in gen(d):
            if pal[-1] == '0' or int(pal[-1]) % 2 == 0:
                continue

            pal = int(pal)
            bn = bin(pal)[2:]
            if bn != bn[::-1]:
                continue
            
            s += pal

    return s

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(solve(n))
