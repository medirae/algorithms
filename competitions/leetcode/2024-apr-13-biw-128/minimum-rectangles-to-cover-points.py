#!/usr/bin/env python3
# https://leetcode.com/problems/minimum-rectangles-to-cover-points/

from typing import *

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        from collections import defaultdict

        # second attempt
        keys = sorted({x for x, _ in points})
        start = keys[0]
        counter = 1
        for x in keys:
            if x - start > w:
                start = x
                counter += 1
        
        return counter

        # first attempt        
        axes = defaultdict(int)
        for x, y in points:
            axes[x] = max(axes[x], y)

        keys = sorted(axes.keys())
        rects = [
            [
                [keys[0], 0],
                [keys[0], axes[keys[0]]]
            ],
        ]
        for x in keys:
            if x - rects[-1][0][0] <= w:
                rects[-1][1][0] = x
            else:
                rects.append([[x, 0], [x, axes[x]]])
        
        return len(rects)

def test():
    tests = [
        [[[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]],1],
        [[[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]],2],
        [[[2,3],[1,2]],0],
    ]
    for t in tests:
        print(*t)
        s = Solution().minRectanglesToCoverPoints(*t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
