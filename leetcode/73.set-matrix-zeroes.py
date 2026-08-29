# Category: algorithms
# Level: Medium
# Percent: 63.337494%



# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# 
# You must do it in place.
# 
#  
# Example 1:
# 
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# 
# 
# Example 2:
# 
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
# 
# 
#  
# Constraints:
# 
# 
# 	m == matrix.length
# 	n == matrix[0].length
# 	1 <= m, n <= 200
# 	-2³¹ <= matrix[i][j] <= 2³¹ - 1
# 
# 
#  
# Follow up:
# 
# 
# 	A straightforward solution using O(mn) space is probably a bad idea.
# 	A simple improvement uses O(m + n) space, but still not the best solution.
# 	Could you devise a constant space solution?
# 
 

# CODE-START
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        return self.flag(matrix)
        return self.bitwise(matrix)
    
    @staticmethod
    def flag(matrix):
        n, m = len(matrix), len(matrix[0])

        r = any(matrix[i][0] == 0 for i in range(n))
        c = any(matrix[0][j] == 0 for j in range(m))

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0

        for i in range(1, n):
            if matrix[i][0] == 0:
                matrix[i][:] = [0] * m
        
        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(1, n):
                    matrix[i][j] = 0
        
        if c:
            matrix[0][:] = [0] * m
        
        if r:
            for i in range(n):
                matrix[i][0] = 0
                
    @staticmethod
    def bitwise(matrix):
        n, m = len(matrix), len(matrix[0])
        r = c = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    r |= 1 << i
                    c |= 1 << j
        
        while r:
            i = r & -r
            r ^= i
            matrix[i.bit_length() - 1][:] = [0] * m

        while c:
            j = c & -c
            c ^= j
            j = j.bit_length() - 1
            for i in range(n):
                matrix[i][j] = 0
        
# CODE-END
