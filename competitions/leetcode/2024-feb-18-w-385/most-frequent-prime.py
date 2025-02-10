#!/usr/bin/env python3
# https://leetcode.com/problems/most-frequent-prime

from typing import *

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        import math
        from collections import deque, Counter
        from itertools import product

        primes = dict()
        def isprime(n):
            if n in primes:
                return primes[n]
            if n <= 1:
                primes[n] = False
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    primes[n] = False
                    return False
            
            primes[n] = True
            return True

        def dfs(row, col, num, dirc: tuple[int] = None):
            nonlocal counter
            if len(num) > 0 and num[0] != '0' and int(num) > 10 and isprime(int(num)):
                counter[int(num)] += 1
            
            if dirc is None:
                for dr, dc in product([-1, 0, 1], repeat=2):
                    if dr == 0 and dc == 0:
                        continue
                    nrow, ncol = row + dr, col + dc
                    if not (0 <= nrow < n and 0 <= ncol < m):
                        continue

                    dfs(nrow, ncol, num + mat[nrow][ncol], (dr, dc))
            else:
                dr, dc = dirc
                nrow, ncol = row + dr, col + dc
                if not (0 <= nrow < n and 0 <= ncol < m):
                    return
                
                dfs(nrow, ncol, num + mat[nrow][ncol], dirc)

        counter = Counter()
        n = len(mat)
        m = len(mat[0])
        mat = [list(map(str, l)) for l in mat]
        for i in range(n):
            for j in range(m):
                dfs(i, j, mat[i][j])

        if not counter:
            return -1
        
        return max((num for num in counter if counter[num] == max(counter.values())))

def test():
    tests = [
        [[1,1],[9,9],[1,1]],
        [[7]],
        [[9,7,8],[4,6,5],[2,8,6]],
    ]
    for t in tests:
        print(t)
        s = Solution().mostFrequentPrime(t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
