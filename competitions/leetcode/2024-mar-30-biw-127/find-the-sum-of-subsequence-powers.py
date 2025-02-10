#!/usr/bin/env python3
# https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

from typing import *

class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        # doesn't work # chat gpt
        mod = 10 ** 9 + 7
        nums.sort()
        n = len(nums)
        
        powers = [[0 for j in range(n)] for i in range(k)]
        for j in range(1, n):
            powers[0][j] = nums[j] - nums[j - 1]
        
        for i in range(1, k):
            for j in range(1, n):
                powers[i][j] = (powers[i][j - 1] + powers[i - 1][j]) % mod
        
        return sum(powers[k - 1][i] for i in range(n)) % mod

def test():
    tests = [
        [[1,2,3,4],3],
        [[2,2],2],
        [[4,3,-1],2],
    ]
    for t in tests:
        print(*t)
        s = Solution().sumOfPowers(*t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
