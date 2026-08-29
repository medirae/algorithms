# Category: algorithms
# Level: Medium
# Percent: 54.340736%



# You are given an m x n integer matrix matrix with the following two properties:
# 
# 
# 	Each row is sorted in non-decreasing order.
# 	The first integer of each row is greater than the last integer of the previous row.
# 
# 
# Given an integer target, return true if target is in matrix or false otherwise.
# 
# You must write a solution in O(log(m * n)) time complexity.
# 
#  
# Example 1:
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# 
# 
# Example 2:
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
# 
# 
#  
# Constraints:
# 
# 
# 	m == matrix.length
# 	n == matrix[i].length
# 	1 <= m, n <= 100
# 	-10⁴ <= matrix[i][j], target <= 10⁴
# 
 

# CODE-START
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        l, r = 0, n - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if matrix[mid][0] <= target:
                l = mid
            else:
                r = mid - 1
        
        if matrix[l][0] == target:
            return True

        i = l
        l, r = 0, m - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if matrix[i][mid] <= target:
                l = mid
            else:
                r = mid - 1

        return matrix[i][l] == target
        
# CODE-END
