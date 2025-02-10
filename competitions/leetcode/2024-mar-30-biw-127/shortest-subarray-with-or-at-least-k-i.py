#!/usr/bin/env python3
# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/

from typing import *

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        from functools import reduce

        n = len(nums)
        for lenn in range(1, n + 1):
            for ndx in range(n - lenn + 1):
                if reduce(lambda x, y: x | y, nums[ndx:ndx + lenn]) >= k:
                    return lenn
        
        return -1

def test():
    tests = [
        [[1,2,3],2],
        [[2,1,8],10],
        [[1,2],0],
    ]
    for t in tests:
        print(*t)
        s = Solution().minimumSubarrayLength(*t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
