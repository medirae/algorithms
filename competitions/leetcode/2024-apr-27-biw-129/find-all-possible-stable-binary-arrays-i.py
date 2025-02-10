#!/usr/bin/env python3
# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/

from typing import *

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        # first attempt: brute force + backtracking + pruning + permutations => TLE
        # the https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/
        #  is the same problem with larger constraints...
        counter = 0
        perm = list()

        def backtrack(zeroes: int, ones: int, consecutive: int):
            if consecutive > limit:
                return
            
            if len(perm) == zero + one:
                nonlocal counter
                counter += 1
                print(perm)
                return

            if ones < one:
                c = consecutive + 1 if (perm and perm[-1] == 1) else 1
                perm.append(1)
                backtrack(zeroes, ones + 1, c)
                perm.pop()
            
            if zeroes < zero:
                c = consecutive + 1 if (perm and perm[-1] == 0) else 1
                perm.append(0)
                backtrack(zeroes + 1, ones, c)
                perm.pop()

        backtrack(0, 0, 0)
        return counter

def test():
    tests = [
        [1,1,2],
        [1,2,1],
        [3,3,2],
    ]
    for t in tests:
        print(*t)
        s = Solution().numberOfStableArrays(*t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
