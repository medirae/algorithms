# Category: algorithms
# Level: Medium
# Percent: 44.77111%



# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# 
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# 
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# 
# The testcases are generated so that the answer will be less than or equal to 2 * 10⁹.
# 
#  
# Example 1:
# 
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# 
# Example 2:
# 
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
# 
# 
#  
# Constraints:
# 
# 
# 	m == obstacleGrid.length
# 	n == obstacleGrid[i].length
# 	1 <= m, n <= 100
# 	obstacleGrid[i][j] is 0 or 1.
# 
 

# CODE-START
class Solution:
    def uniquePathsWithObstacles(self, mx: list[list[int]]) -> int:
        n, m = len(mx), len(mx[0])

        mx[0][0] = int(not mx[0][0])
        for j in range(1, m):
            mx[0][j] = mx[0][j - 1] if mx[0][j] == 0 else 0

        for i in range(1, n):
            for j in range(m):
                if mx[i][j] == 0:
                    mx[i][j] = (
                        (mx[i - 1][j] if 0 < i else 0) +
                        (mx[i][j - 1] if 0 < j else 0)
                    )
                else:
                    mx[i][j] = 0

        return mx[n - 1][m - 1]
# CODE-END
