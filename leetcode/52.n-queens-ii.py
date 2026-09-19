# Category: algorithms
# Level: Hard
# Percent: 79.01344%



# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# 
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
# 
#  
# Example 1:
# 
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# 
# 
# Example 2:
# 
# Input: n = 1
# Output: 1
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= n <= 9
# 
 

# CODE-START
class Solution:
    def totalNQueens(self, n: int) -> int:
        mask = (1 << n) - 1
        def bt(r=0, cs=0, uls=0, dls=0):
            # rows, columns, upward lines, downward lines
            if r == n:
                return 1
            
            count = 0
            av = mask ^ (cs | uls | dls)
            while av:
                c = av & -av
                av ^= c
                cndx = c.bit_length() - 1
                count += bt(
                    r + 1,
                    cs | c,
                    mask & ((uls | c) << 1),
                    (dls | c) >> 1,
                )

            return count
        
        return bt()
# CODE-END
