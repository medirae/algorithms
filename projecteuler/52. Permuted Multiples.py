"""
n = a1a2...ak

-   x * n
    
    1 <= i <= k
    A(i) = i-th digit of n
    C(i) = carry
    D(i) = i-th digit of product
    
    C(k) = 0
    for i in k..1
        p = x * A(i)
        C(i) = m // 10
        D(i) = (m % 10) * 10^(k - i) + C(i - 1)

-   2 <= x <= 6
    C(0) must be zero
    {i=1:k | D(i)} must be {i=1:k | A(i)}
"""

def solve() -> int:
    k = 1

    while True:
        mi = 10 ** (k - 1)
        ma = (10 ** k - 1) // 6

        for n in range(mi, ma + 1):
            digits = sorted(str(n))

            if all(
                digits == sorted(str(m * n))
                for m in range(2, 7)
            ):
                return n

        k += 1

if __name__ == '__main__':
    print(solve())
