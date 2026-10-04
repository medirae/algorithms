"""
abcdef
abc|cba 
    a: a * (100000) + a * (1)   = a*100001
    b: b * (10000)  + b * (10)  = b*10010
    c: c * (1000)   + c * (100) = c*1100

    -> a100001 + b10010 + c1100
     = a * 11 * 9091 + b * 11 * 910 + c * 11 * 100
     = 11 * (a9091 + b910 + c100)
"""

def largest_palindrome():
    m = 0
    for i in range(90, 9, -1):
        for j in range(999, 99, -1):
            p = 11 * i * j
            if p < m:
                break

            ps = str(p)
            if ps == ps[::-1]:
                m = p

    return m

if __name__ == '__main__':
    print(largest_palindrome())
