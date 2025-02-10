#!/usr/bin/env python3
# https://leetcode.com/problems/apply-operations-to-make-string-empty

from typing import *

class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        from collections import Counter
        counter = Counter(s)
        maxs = max(counter.values())
        ans = list()
        visited = set()
        for ndx in range(len(s) - 1, -1, -1):
            if counter[s[ndx]] == maxs and s[ndx] not in visited:
                ans.append(s[ndx])
                visited.add(s[ndx])

        return "".join(ans[::-1])

def test():
    tests = [
        "aabcbbca",
        'abcd',
    ]
    for t in tests:
        print(t)
        s = Solution().lastNonEmptyString(t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
