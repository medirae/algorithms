# Category: algorithms
# Level: Hard
# Percent: 76.04219%



# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# 
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# 
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
# 
#  
# Example 1:
# 
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# 
# 
# Example 2:
# 
# Input: n = 1
# Output: [["Q"]]
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
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        if n == 2 or n == 3:
            return list()
        
        return self.bitwise(n)
        return self.straight(n)

    @staticmethod
    def bitwise(n):
        mask = (1 << n) - 1
        o = list()
        p = [None] * n
        def bt(r=0, cs=0, uls=0, dls=0):
            # row, columns, upward lines, downward lines

            if r == n:
                o.append(p.copy())
                return

            av = mask ^ (cs | uls | dls)
            while av:
                c = av & -av
                av ^= c
                cndx = c.bit_length() - 1
                p[r] = f'{"." * cndx}Q{"." * (n - cndx - 1)}'
                bt(
                    r + 1,
                    cs | c,
                    mask & ((uls | c) << 1),
                    (dls | c) >> 1
                )

        bt()
        return o

    @staticmethod
    def straight(n):
        o = list()
        p = [["."] * n for _ in range(n)]
        cs = uls = dls = 0  # columns, upward lines, downward lines
        def bt(r=0):
            if r == n:
                o.append([''.join(er) for er in p])
                return

            nonlocal cs, uls, dls
            for c in range(n):
                cb, ulb, dlb = 1 << c, 1 << (r + c), 1 << (r + n - 1 - c)
                if cs & cb or uls & ulb or dls & dlb:
                    continue
                cs, uls, dls = cs | cb, uls | ulb, dls | dlb
                p[r][c] = "Q"
                bt(r + 1)
                p[r][c] = "."
                cs, uls, dls = cs ^ cb, uls ^ ulb, dls ^ dlb

        bt()
        return o
        
# CODE-END
