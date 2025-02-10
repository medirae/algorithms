#!/usr/bin/env python3
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii

from typing import *

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        from heapq import heappop, heappush, heapify
        heapify(nums)
        counter = 0
        while len(nums) >= 2 and nums[0] < k:
            a = heappop(nums)
            b = heappop(nums)
            heappush(nums, 2 * min(a, b) + max(a, b))
            counter += 1
        
        return counter

def test():
    tests = [
        [[2,11,10,1,3],10],
        [[1,1,2,4,9],20],
    ]
    for t in tests:
        print(*t)
        s = Solution().minOperations(*t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
