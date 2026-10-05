from math import isqrt

primes = [2]

def next_prime() -> int:
    candidate = primes[-1] + 1
    candidate += candidate % 2 == 0
    
    while True:
        limit = isqrt(candidate)
        isp = True
        for p in primes:
            if p > limit:
                break
            if candidate % p == 0:
                isp = False
                break

        if isp:
            primes.append(candidate)
            return candidate

        candidate += 2

def summation_primes(n: int) -> set:
    s = 2
    while (v := next_prime()) < n:
        s += v

    return s

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(summation_primes(n))
