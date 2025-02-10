#!/usr/bin/env python3
# https://leetcode.com/problems/make-a-square-with-the-same-color/

from typing import *

class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for row in range(2):
            for col in range(2):
                counter = Counter([grid[row + r][col + c] for r, c in ((0, 0), (0, 1), (1, 0), (1, 1))])
                if counter['B'] >= 3 or counter['W'] >= 3:
                    return True
        
        return False

def test():
    tests = [
        # [["B","W","B"],["B","W","W"],["B","W","B"]],
        # [["B","W","B"],["W","B","W"],["B","W","B"]],
        # [["B","W","B"],["B","W","W"],["B","W","W"]],
        [["B","W","B"],["B","W","W"],["B","W","B"]]
    ]
    for t in tests:
        print(*t, sep='\n', end='\n\n')
        s = Solution().canMakeSquare(t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
