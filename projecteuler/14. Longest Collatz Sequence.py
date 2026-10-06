from math import log2, floor

cache = {1: 1}

def chain_len(n: int) -> int:
    if n in cache:
        return cache[n]
    
    x = floor(log2(n & -n))
    an = n // pow(2, x)
    if an > 1:
        cache[n] = 1 + x + chain_len(3 * an + 1)
    else:
        cache[n] = x + cache[1]

    return cache[n]

def max_chain_len(n: int) -> int:
    ma_len = ma_val = 1
    for i in range(2, n + 1):
        if (ln := chain_len(i)) > ma_len:
            ma_len, ma_val = ln, i

    return ma_val

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(max_chain_len(n))
