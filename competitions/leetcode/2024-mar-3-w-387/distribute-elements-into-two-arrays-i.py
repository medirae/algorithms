#!/usr/bin/env python3
# https://leetcode.com/problems/distribute-elements-into-two-arrays-i

from typing import *

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [nums[0]], [nums[1]]
        for ndx in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[ndx])
            else:
                arr2.append(nums[ndx])
        
        return arr1 + arr2

def test():
    tests = [
        [2,1,3],
        [5,4,3,8],
    ]
    for t in tests:
        print(t)
        s = Solution().resultArray(t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
