"""
sum:
    odd + odd: even
        2k + 1 + 2j + 1 = 2(k + j)
    odd + even: odd
        2k + 1 + 2j     = 2(k + j) + 1
    even + even: even
        2k + 2j = 2(k + j)

fib: 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584
     o e o o e  o  o  e  o  o   e   o   o   e   o    o    e

from 5 <= i -> even fib: i = 2 + 3k

fib(i) <= 4,000,000 -> fib(32) = 3524578 -> i = 32

maximum even index:
       2 + 3k <= 32
    -> 3k <= 30
    -> k <= 10
    -> max i = 32

even sum:
       2 + sum(k=1:10, fib(3k + 2))
"""

def fib_even_sum(maximum_value: int) -> int:
    a, b = 1, 2
    s = 0
    i = 2
    while b <= maximum_value:
        if (i - 2) % 3 == 0:
            s += b
        a, b = b, a + b
        i += 1

    return s

if __name__ == '__main__':
    maxvalue = int(input("enter maximum fibonacci value: "))
    print(fib_even_sum(maxvalue))
