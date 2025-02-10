#!/usr/bin/env python3

from math import ceil

"""
1234
n = 4
m = 2
w = 10^2
number = 34 + 12*10^2 = 3400

12345
n = 5
m = 3
123 45
w = 10^3
number = 345 + 12*10^3 = 12345
"""
def dissect_number(number: int):
    number_str = str(number)
    if len(number_str) % 2 == 1:
        number_str = f'0{number_str}'

    n = len(number_str)
    m = n // 2
    w = 10 ** m
    first = int(number_str[:m])
    second = int(number_str[m:])
    return n if number_str[0] != 0 else n - 1, w, first, second

def fast_multiplication(a: int, b: int):
    n, aw, a1, a0 = dissect_number(a)
    m, bw, b1, b0 = dissect_number(b)
    if n <= 2 or m <= 2:
        print(a0*b0, a0*b1*bw, b0*a1*aw, a1*aw*b1*bw, a0*b0 + a0*b1*bw + b0*a1*aw + a1*aw*b1*bw)
        return a0*b0 + a0*b1*bw + b0*a1*aw + a1*aw*b1*bw
    
    t1 = fast_multiplication(a0, b0)
    t2 = fast_multiplication(a0, b1)
    t3 = fast_multiplication(b0, a1)
    t4 = fast_multiplication(a1, b1)
    print(t1, t2*bw, t3*aw, t4*aw*bw, t1 + t2*bw + t3*aw + t4*aw*bw)
    return t1 + t2*bw + t3*aw + t4*aw*bw

if __name__ == '__main__':
    a = 12345678909876543212345678909876543421234567890987654321
    b = 98765432123456789876543212345467898765432123456789876543
    m = fast_multiplication(a, b)
    assert a * b == m