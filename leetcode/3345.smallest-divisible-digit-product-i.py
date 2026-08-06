# Category: algorithms
# Level: Easy
# Percent: 64.62409%



# You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.
# 
#  
# Example 1:
# 
# 
# Input: n = 10, t = 2
# 
# Output: 10
# 
# Explanation:
# 
# The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.
# 
# 
# Example 2:
# 
# 
# Input: n = 15, t = 3
# 
# Output: 16
# 
# Explanation:
# 
# The digit product of 16 is 6, which is divisible by 3, making it the smallest number greater than or equal to 15 that satisfies the condition.
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= n <= 100
# 	1 <= t <= 10
# 
 

# CODE-START
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        n, x1 = divmod(n, 10)
        n, x10 = divmod(n, 10)
        while (max(x10, 1) * x1) % t != 0:
            x10 += (x1 + 1) // 10
            x1 = (x1 + 1) % 10
        return 100 * n + 10 * x10 + x1

        def primes(n):
            # TODO :)

            # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
            """ Returns  a list of primes < n """
            sieve = [True] * n
            for i in range(3,int(n**0.5)+1,2):
                if sieve[i]:
                    sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
            ps = [2] + [i for i in range(3,n,2) if sieve[i]]
            pn = len(ps)
            pndx = 0
            p = dict()
            while n > 1 and pndx < pn:
                while pndx < pn and ps[pndx] <= n and n % ps[pndx] != 0:
                    pndx += 1
                c = 0
                while n > 1 and pndx < pn and n % ps[pndx] == 0:
                    n //= ps[pndx]
                    c += 1
                if pndx < pn and c > 0:
                    p[ps[pndx]] = c
            return p

        n_primes = primes(n)
        t_primes = primes(t)
        diff = dict()
        for num, count in t_primes.items():
            if num not in n_primes:
                diff[num] = count
            elif count > n_primes[num]:
                diff[num] = count - n_primes[num]

        denom = {
            9: (3, 2), 
        }

        for i in range(1, 100):
            x10, x1 = divmod(i, 10)
            print(i, primes(i))
            print(x1, primes(x1))
            print(x10, primes(x10))
            print()

        td = primes(t) or [1]

        s = str(n)
        dg = [0] * len(s)
        for ndx, c in enumerate(s):
            dg[ndx] = ord(c) - 48

        return 0

        p, m, xk = 1, n, n % 10
        while m:
            m, d = divmod(m, 10)
            p *= d

        print(f'{xk=} {p=}')
        print(f'{p % t=} {(t - (xk % t)) % t=}')
        return n + int((p % t) != 0) * min(
            10 - xk,
            (t - (xk % t)) % t,
        )
        
# CODE-END
