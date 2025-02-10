#!/usr/bin/env python3
# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii

from typing import *

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        storage = dict()
        def back(start: int, end: int):
            if end - start + 1 < 2:
                return 0

            if (start, end) in storage:
                return storage[(start, end)]

            maximum = 0
            nonlocal score
            if sum(nums[start:start + 2]) == score:
                maximum = max(maximum, 1 + back(start + 2, end))
            
            if sum(nums[end - 1:end + 1]) == score:
                maximum = max(maximum, 1 + back(start, end - 2))
            
            if nums[start] + nums[end] == score:
                maximum = max(maximum, 1 + back(start + 1, end - 1))

            storage[(start, end)] = maximum
            return maximum

        maximum = 0
        score = sum(nums[:2])
        maximum = max(maximum, 1 + back(2, n - 1))
        storage.clear()
        score = sum(nums[-2:])
        maximum = max(maximum, 1 + back(0, n - 3))
        storage.clear()
        score = nums[0] + nums[-1]
        maximum = max(maximum, 1 + back(1, n - 2))
        return maximum

def test():
    tests = [
        [3,2,1,2,3,4],
        [3,2,6,1,4],
    ]
    for t in tests:
        print(t)
        s = Solution().maxOperations(t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
