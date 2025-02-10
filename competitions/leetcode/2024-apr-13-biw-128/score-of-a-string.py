#!/usr/bin/env python3
# https://leetcode.com/problems/score-of-a-string

from typing import *

class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(map(lambda x: abs(ord(x[0]) - ord(x[1])), zip(s[:-1], s[1:])))

def test():
    tests = [
        'hello',
        'zaz'
    ]
    for t in tests:
        print(t)
        s = Solution().scoreOfString(t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
