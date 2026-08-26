# Category: algorithms
# Level: Medium
# Percent: 57.313%



# Given an m x n matrix, return all elements of the matrix in spiral order.
# 
#  
# Example 1:
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
#  
# Constraints:
# 
# 
# 	m == matrix.length
# 	n == matrix[i].length
# 	1 <= m, n <= 10
# 	-100 <= matrix[i][j] <= 100
# 
 

# CODE-START
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        o = [0] * (m * n)
        mr = min((n + 1) // 2, (m + 1) // 2)
        ndx = 0
        for r in range(mr):
            o[ndx:ndx + m - 2 * r] = matrix[r][r:m - r]
            ndx += m - 2 * r
            if n - 2 * r > 1:
                for i in range(r + 1, n - r):
                    o[ndx + i - r - 1] = matrix[i][m - 1 - r]
                ndx += n - 2 * r - 1
            if m - 2 * r > 1 and n - 2 * r > 1:
                o[ndx:ndx + m - 2 * r - 1] = matrix[n - 1 - r][m - r - 2:r - 1 if r > 0 else None:-1]
                ndx += m - 2 * r - 1
            if n - 2 * r > 2 and m - 2 * r > 1:
                for i in range(n - r - 2, r, -1):
                    o[ndx + n - r - i - 2] = matrix[i][r]
                ndx += n - 2 * r - 2

        return o
        
# CODE-END
