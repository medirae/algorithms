#!/usr/bin/env python3
# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k

from typing import *

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        counter = 0
        storage = [[0 for j in range(m)] for i in range(n)]

        summ = 0
        for j in range(m):
            summ += grid[0][j]
            storage[0][j] = summ
            if storage[0][j] <= k:
                counter += 1
        summ = 0
        for i in range(n):
            summ += grid[i][0]
            storage[i][0] = summ
            if i >= 1 and storage[i][0] <= k:
                counter += 1

        for i in range(1, n):
            for j in range(1, m):
                storage[i][j] = storage[i - 1][j] + storage[i][j - 1] - storage[i - 1][j - 1] + grid[i][j]
                if storage[i][j] <= k:
                    counter += 1

        return counter

def test():
    tests = [
        [[[7,6,3],[6,6,1]],18],
        [[[7,2,9],[1,5,0],[2,6,6]],20],
        [[[6],[5]],9]
    ]
    for t in tests:
        print(*t)
        s = Solution().countSubmatrices(*t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
