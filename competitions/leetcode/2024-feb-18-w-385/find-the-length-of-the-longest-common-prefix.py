#!/usr/bin/env python3
# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix

from typing import *

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = list(map(str, arr1))
        arr2 = list(map(str, arr2))
        root = dict()
        for number in arr1:
            node = root
            for char in number:
                if char not in node:
                    node[char] = dict()
                node = node[char]
            node['isnum'] = True

        maximum = 0
        for number in arr2:
            node = root
            counter = 0
            for char in number:
                if char not in node:
                    break
                node = node[char]
                counter += 1
            maximum = max(maximum, counter)

        return maximum

def test():
    tests = [
        [[1,10,100],[1000]],
        [[1,2,3],[4,4,4]],
        [[5655359], [56554]],
    ]
    for t in tests:
        print(*t)
        s = Solution().longestCommonPrefix(*t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
