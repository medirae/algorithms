# Category: algorithms
# Level: Medium
# Percent: 74.13702%



# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# 
# The area of an island is the number of cells with a value 1 in the island.
# 
# Return the maximum area of an island in grid. If there is no island, return 0.
# 
#  
# Example 1:
# 
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# 
# 
# Example 2:
# 
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
# 
# 
#  
# Constraints:
# 
# 
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 50
# 	grid[i][j] is either 0 or 1.
# 
 

# CODE-START
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            o = 1
            if i + 1 < n and grid[i + 1][j]:
                grid[i + 1][j] = False
                o += dfs(i + 1, j)
            if i - 1 >=0 and grid[i - 1][j]:
                grid[i - 1][j] = False
                o += dfs(i - 1, j)
            if j + 1 < m and grid[i][j + 1]:
                grid[i][j + 1] = False
                o += dfs(i, j + 1)
            if j - 1 >=0 and grid[i][j - 1]:
                grid[i][j - 1] = False
                o += dfs(i, j - 1)
            
            return o
            
        mi = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    grid[i][j] = False
                    mi = max(mi, dfs(i, j))
        
        return mi
        
# CODE-END
