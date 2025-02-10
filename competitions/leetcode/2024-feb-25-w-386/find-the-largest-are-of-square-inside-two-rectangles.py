#!/usr/bin/env python3
# https://leetcode.com/problems/find-the-largest-area-of-two-squares-inside-two-rectangles

from typing import *

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        max_area = 0
        n = len(bottomLeft)

        def intersectArea(rect1, rect2):
            x_overlap = max(0, min(rect1[1][0], rect2[1][0]) - max(rect1[0][0], rect2[0][0]))
            y_overlap = max(0, min(rect1[1][1], rect2[1][1]) - max(rect1[0][1], rect2[0][1]))
            return x_overlap * y_overlap

        for i in range(n):
            for j in range(i + 1, n):
                intersection_area = intersectArea([bottomLeft[i], topRight[i]], [bottomLeft[j], topRight[j]])
                max_area = max(max_area, min(topRight[i][0] - bottomLeft[i][0], topRight[i][1] - bottomLeft[i][1], 
                           topRight[j][0] - bottomLeft[j][0], topRight[j][1] - bottomLeft[j][1]) ** 2)
                print(f'{i=} {j=} {intersection_area=} {max_area=}')

def test():
    tests = [
        [[[1,1],[2,2],[3,1]],[[3,3],[4,4],[6,6]]],
        [[[1,1],[2,2],[1,2]],[[3,3],[4,4],[3,4]]],
        [[[1,1],[3,3],[3,1]],[[2,2],[4,4],[4,2]]],
    ]
    for t in tests:
        print(*t)
        s = Solution().largestSquareArea(*t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
