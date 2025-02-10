#!/usr/bin/env python3
# https://leetcode.com/problems/earliest-second-to-mark-indices-i

from typing import *

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n = len(nums)
        m = len(changeIndices)

        marked = [False] * n
        if set(changeIndices) != set(range(1, n + 1)):
            return -1
        for s in range(m):
            nums[changeIndices[s] - 1] -= 1
            if nums[changeIndices[s] - 1] == 0:
                marked[changeIndices[s] - 1] = True
            if all(marked):
                return s + 1
        
        return -1

def test():
    tests = [
        [[2,2,0],[2,2,2,2,3,2,2,1]],
        [[1,3],[1,1,1,2,1,1,1]],
        [[0,1],[2,2,2]],
    ]
    for t in tests:
        print(*t)
        s = Solution().earliestSecondToMarkIndices(*t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
