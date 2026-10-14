"""
F(1) = 1 + 1/2
F(2) = 1 + 1 / (1 + 1 + 1/2) = 1 + 1 / (1 + F(1))
F(3) = 1 + 1 / (1 + 1 + 1 / (1 + 1 + 1/2) = 1 + 1 / (1 + F(2))

-   F(n) = 1 + 1 / (1 + F(n - 1))

-   N(n) = numenator of F(n)
    D(n) = denominator of D(n)
    F(n) = N(n) / D(n)
         = 1 + 1 / (1 + N(n - 1) / D(n - 1))
         = 1 + 1 / (D(n - 1) + N(n - 1) / D(n - 1))
         = 1 + D(n - 1) / (D(n - 1) + N(n - 1))
         = [ D(n - 1) + N(n - 1) + D(n - 1) ] / [ D(n - 1) + N(n - 1) ]
         = [ N(n - 1) + 2D(n - 1) ] / [ N(n - 1) + D(n - 1) ]
    
    N(n) = N(n - 1) + 2 * D(n - 1)
    D(n) = N(n - 1) + D(n - 1)
"""

def solve(n: int) -> int:
    c = 0
    nu, de = 1, 1
    for _ in range(n):
        nu, de = nu + 2 * de, nu + de
        c += len(str(nu)) > len(str(de))

    return c

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(solve(n))
