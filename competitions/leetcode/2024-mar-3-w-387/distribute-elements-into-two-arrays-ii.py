#!/usr/bin/env python3
# https://leetcode.com/problems/distribute-elements-into-two-arrays-ii

from typing import *

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        from collections import Counter
        
        arr1, arr2 = [nums[0]], [nums[1]]
        c1, c2 = Counter(arr1), Counter(arr2)
        oc1, oc2 = Counter(), Counter()
        oc1[nums[0]] = 0
        oc2[nums[1]] = 0

        for ndx in range(2, len(nums)):
            oc1[nums[ndx]] = sum(1 for x in arr1 if x < nums[ndx])
            oc2[nums[ndx]] = sum(1 for x in arr2 if x < nums[ndx])

            if oc1[nums[ndx]] > oc2[nums[ndx]]:
                arr1.append(nums[ndx])
                c1[nums[ndx]] += 1
            elif oc1[nums[ndx]] < oc2[nums[ndx]]:
                arr2.append(nums[ndx])
                c2[nums[ndx]] += 1
            elif len(arr1) > len(arr2):
                arr2.append(nums[ndx])
                c2[nums[ndx]] += 1
            else:
                arr1.append(nums[ndx])
                c1[nums[ndx]] += 1

        return arr1 + arr2

def test():
    tests = [
        [2,1,3,3],
        [5,14,3,1,2],
        [3,3,3,3],
    ]
    for t in tests:
        print(t)
        s = Solution().resultArray(t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
