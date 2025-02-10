#!/usr/bin/env python3
# https://leetcode.com/problems/minimum-levels-to-gain-more-points/

from typing import *

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        possible = [1 if num else -1 for num in possible]
        n = len(possible)
        points = [0] * n
        
        summ = sum(possible)
        points[0] = possible[0]
        for ndx in range(1, n):
            points[ndx] = points[ndx - 1] + possible[ndx]

        for ndx in range(n - 1):
            dan = points[ndx]
            bob = summ - dan
            if dan > bob:
                return ndx + 1
        
        return -1
        

def test():
    tests = [
        [1,0,1,0],
        [1,1,1,1,1],
        [0,0],
        [0,0,1],
    ]
    for t in tests:
        print(t)
        s = Solution().minimumLevels(t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
