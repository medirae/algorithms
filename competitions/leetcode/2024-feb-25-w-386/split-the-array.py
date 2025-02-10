#!/usr/bin/env python3
# https://leetcode.com/problems/split-the-array

from typing import *

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        from collections import Counter

        if len(nums) % 2 != 0:
            return False

        counter = Counter(nums)
        if any(map(lambda x: counter[x] > 2, counter.keys())):
            return False
        return True

def test():
    tests = [
        [1,1,2,2,3,4],
        [1,1,1,1],
        [1,2,3,3,7,8,5,6],
    ]
    for t in tests:
        print(t)
        s = Solution().isPossibleToSplit(t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
