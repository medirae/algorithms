#!/usr/bin/env python3
# https://leetcode.com/problems/right-triangles/

from typing import *

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        from itertools import product
        n, m = len(grid), len(grid[0])
        rows, cols = [set() for i in range(n)], [set() for j in range(m)]
        for i, j in product(range(n), range(m)):
            if grid[i][j]:
                rows[i].add(j)
                cols[j].add(i)

        counter = 0
        for i, j in product(range(n), range(m)):
            if not grid[i][j] or len(rows[i]) <= 1 or len(cols[j]) <= 1:
                continue
                
            counter += (len(rows[i]) - 1) * (len(cols[j]) - 1)

        return counter


def test():
    tests = [
        [[0,1,0],[0,1,1],[0,1,0]],
        [[1,0,0,0],[0,1,0,1],[1,0,0,0]],
        [[1,0,1],[1,0,0],[1,0,0]],
    ]
    for t in tests:
        print(*t, sep='\n')
        s = Solution().numberOfRightTriangles(t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
