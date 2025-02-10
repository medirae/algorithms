#!/usr/bin/env python3
# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i

from typing import *

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        score = nums[0] + nums[1]
        counter = 1
        nums = nums[2:]
        while len(nums) >= 2:
            a, b = nums[:2]
            if a + b == score:
                counter += 1
                nums = nums[2:]
            else:
                break
        
        return counter

def test():
    tests = [
        [3,2,1,4,5],
        [3,2,6,1,4],
        [2,2,3,2,4,2,3,3,1,3],
    ]
    for t in tests:
        print(t)
        s = Solution().maxOperations(t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
