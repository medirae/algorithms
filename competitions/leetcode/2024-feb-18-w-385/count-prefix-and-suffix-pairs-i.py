#!/usr/bin/env python3
# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i

from typing import *

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:        
        return len([(i, j) for i in range(len(words)) for j in range(i + 1, len(words))
                    if words[j].startswith(words[i]) and words[j].endswith(words[i])])


def test():
    tests = [
        ["a","aba","ababa","aa"],
        ["pa","papa","ma","mama"],
        ["abab","ab"],
    ]
    for t in tests:
        print(*t)
        s = Solution().countPrefixSuffixPairs(t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
