from math import sqrt, ceil

primes = {2}

def check_prime(n: int) -> bool:
    if n in primes:
        return True

    for i in primes:
        if n % i == 0:
            return False

    primes.add(n)
    return True

def nth_prime(n: int) -> set:
    v = 2
    for _ in range(n):
        while not check_prime(v):
            v += 1
        
        v += 1

    return v - 1

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(nth_prime(n))
